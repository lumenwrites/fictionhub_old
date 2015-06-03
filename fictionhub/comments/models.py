from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from django.db.models import permalink

class Comment(models.Model):
    story = models.ForeignKey('Story', related_name="comments",
                              default=None, null=True, blank=True)
    chapter = models.ForeignKey('Chapter', related_name="comments",
                                default=None,  null=True, blank=True)    
    parent = models.ForeignKey('Comment', related_name="children",
                               default=None, null=True, blank=True)
    body = models.TextField()    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments")
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    COMMENT_TYPES = (
    (u'1', u'Comment'),
    (u'2', u'Review'),
    )    
    comment_type = models.CharField(max_length=64, default="Comment", choices=COMMENT_TYPES)

    def __str__(self):
        string_name = ""
        try:
            string_name = self.body # self.story.title + self.body
        except:
            string_name = self.body # self.chapter.title + self.body  
        return string_name
