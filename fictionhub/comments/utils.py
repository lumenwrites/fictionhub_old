from posts.utils import rank_hot, rank_top
from django.core.mail import send_mail # for email
from django.http import HttpResponseRedirect

from notifications.models import Message

from .models import Comment
from .forms import CommentForm

def submit_comment(request, post):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # return post but don't save it to db just yet
            comment.author = request.user
            comment.parent = None
            comment.post = post                
            comment.save()
            # Send Email
            # if comment.post.author.email_comments:
            #     commentauthor = comment.author.username
            #     topic = commentauthor + " has commented on your story "
            #     body = commentauthor + " has left a comment on your story\n" +\
            #            "http://fictionhub.io"+comment.post.get_absolute_url()+ "\n" +\
            #            "'" + comment.body[:64] + "...'"
            #     body += "\n\nYou can manage your email notifications in preferences:\n" +\
            #             "http://fictionhub.io/preferences/"
            #     try:
            #         email = comment.post.author.email            
            #         send_mail(topic, body, 'raymestalez@gmail.com', [email], fail_silently=False)
            #     except:
            #         pass
            # Notification
            message = Message(from_user=request.user,
                              to_user=comment.post.author,
                              story=comment.post,
                              comment=comment,
                              message_type="comment")
            message.save()
            comment.post.author.new_notifications = True
            comment.post.author.save()
            

            if post.post_type == "chapter":
                return HttpResponseRedirect('/story/'+post.parent.slug+'/'+post.slug+'#comments')
            else:
                return HttpResponseRedirect('/story/'+post.slug+'#comments')
                
    

def get_comment_list(comments=None, rankby="hot"):
    """Recursively build a list of comments."""
    yield 'in'

    # Loop through all the comments I've passed
    for comment in comments:
        # Add comment to the list
        yield comment
        # get comment's children
        children = comment.children.all()
        if rankby == "hot":
            ranked_children = rank_hot(children, top=32)
        elif rankby == "top":
            ranked_children = rank_top(children, timespan = "all-time")
        elif rankby == "new":
            ranked_children = children.order_by('-pub_date')
        else:
            ranked_children = []
        
        # If there's any children
        if len(ranked_children):
            comment.leaf=False
            # loop through children, and apply this function
            for x in get_comment_list(ranked_children, rankby=rankby):
                yield x
        else:
            comment.leaf=True
    yield 'out'

def get_comments(post, rankby="new",comment_id=None):
    top_lvl_comments = Comment.objects.filter(post = post, parent = None)

    # Rank comments
    if rankby == "hot":
        ranked_comments = rank_hot(top_lvl_comments, top=32)
    elif rankby == "top":
        ranked_comments = rank_top(top_lvl_comments, timespan = "all-time")
    elif rankby == "new":
        ranked_comments = top_lvl_comments.order_by('-pub_date')
    else:
        ranked_comments = []

    # Permalink to one comment
    if comment_id:
        comment = []
        comment.append(Comment.objects.get(id = comment_id))
        ranked_comments = comment


    # Nested comments
    comments = list(get_comment_list(ranked_comments, rankby=rankby))
        
    return comments

def send_comment_email_notification(comment):
    if comment.parent.author.email_comments:
        commentauthor = comment.author.username
        topic = commentauthor + " has replied to your comment"
        body = commentauthor + " has replied to your comment\n" +\
               "http://fictionhub.io"+comment.post.get_absolute_url()+ "\n" +\
               "'" + comment.body[:64] + "...'"
        body += "\n\nYou can manage your email notifications in preferences:\n" +\
                "http://fictionhub.io/preferences/"
        try:
            email = comment.parent.author.email            
            send_mail(topic, body, 'raymestalez@gmail.com', [email], fail_silently=False)
        except:
            pass
