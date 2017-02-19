import praw, time, os

from .models import Post

from django.http import HttpResponseRedirect

def post_to_reddit(request, story):
    post = Post.objects.get(slug=story)

    # throw him out if he's not an author
    if request.user != post.author:
        return HttpResponseRedirect('/')        


    r = praw.Reddit(user_agent='Post /r/WritingPrompts story by /u/raymestalez')
    r.login(os.environ["LUMENUNAME"],os.environ["LUMENPASS"])
    # subreddit = r.get_subreddit('WritingPrompts')
    submission = r.get_submission(post.reddit_url)
    submission.add_comment(post.body)
    time.sleep(1)
    
    return HttpResponseRedirect(post.reddit_url)



