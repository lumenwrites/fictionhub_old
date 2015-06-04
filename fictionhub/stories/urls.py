from django.conf.urls import url

from . import views

urlpatterns = [
    # Comments
    url(r'^comment-submit/(?P<comment_id>[^\.]+)', views.comment_submit),
    url(r'^comment-upvote/', views.comment_upvote),
    url(r'^comment-downvote/', views.comment_downvote),
    url(r'^comment-unupvote/', views.comment_unupvote),
    url(r'^comment-undownvote/', views.comment_undownvote),

    url(r'^comment/(?P<comment_id>[^\.]+)/edit', views.comment_edit),
    url(r'^comment/(?P<comment_id>[^\.]+)/delete', views.comment_delete), 
    
    # view comment
    url(r'^story/(?P<story>[^\.]+)/comment/(?P<comment_id>[^\.]+)', views.story),

    url(r'^user/(?P<username>[^\.]+)/comments$', views.comments_user,
        {'filterby': 'comments_user'}),
    
    # Edit story
    url(r'^story/add$', views.story_create),
    url(r'^story/(?P<story>[^\.]+)/(?P<chapter>[^\.]+)/edit$', views.chapter_edit),    
    url(r'^story/(?P<story>[^\.]+)/(?P<chapter>[^\.]+)/up$', views.chapter_up),
    url(r'^story/(?P<story>[^\.]+)/(?P<chapter>[^\.]+)/down$', views.chapter_down),
    url(r'^story/(?P<story>[^\.]+)/(?P<chapter>[^\.]+)/delete$', views.chapter_delete),        
    
    url(r'^story/(?P<story>[^\.]+)/edit$', views.story_edit),
    url(r'^story/(?P<story>[^\.]+)/delete$', views.story_delete),
    url(r'^story/(?P<story>[^\.]+)/publish$', views.story_publish),
    url(r'^story/(?P<story>[^\.]+)/unpublish$', views.story_unpublish),          
    url(r'^story/(?P<story>[^\.]+)/add$', views.chapter_create),

    url(r'^hub/add/$', views.hub_create),    

    # View
    # url(r'^story/(?P<story>[^\.]+)/(?P<chapter>[^\.]+)$', views.chapter),

    # Rss
    url(r'^story/(?P<story>[^\.]+)/feed$', views.story_feed),        

    url(r'^404/', views.page_404),
    
    # Rank comments
    url(r'^story/(?P<story>[^\.]+)/(?P<chapter>[^\.]+)/comments/(?P<rankby>[^\.]+)$',
        views.story, name='view_chapter'), 
    url(r'^story/(?P<story>[^\.]+)/comments/(?P<rankby>[^\.]+)$', views.story, name='view_story'),    
    # View story/chapter
    url(r'^story/(?P<story>[^\.]+)/(?P<chapter>[^\.]+)$', views.story, name='view_chapter'), 
    url(r'^story/(?P<story>[^\.]+)$', views.story, name='view_story'),    

    url(r'^upvote/$', views.upvote),
    url(r'^downvote/$', views.downvote),
    url(r'^unupvote/$', views.unupvote),
    url(r'^undownvote/$', views.undownvote),

    # List stories
    # User
    # Subscriptions
    url(r'^user/(?P<username>[^\.]+)/(?P<rankby>[^\.]+)/(?P<timespan>[^\.]+)/$', views.stories,
        {'filterby': 'user'}),    
    url(r'^user/(?P<username>[^\.]+)/(?P<rankby>[^\.]+)/$', views.stories,
        {'filterby': 'user'}),    
    url(r'^user/(?P<username>[^\.]+)/$', views.stories,
        {'filterby': 'user'}),    
    
    # Subscriptions
    url(r'^subscriptions/(?P<rankby>[^\.]+)/(?P<timespan>[^\.]+)/$', views.stories,
        {'filterby': 'subscriptions'}),    
    url(r'^subscriptions/(?P<rankby>[^\.]+)/$', views.stories,
        {'filterby': 'subscriptions'}),    
    url(r'^subscriptions/$', views.stories,
        {'filterby': 'subscriptions'}),    

    # By hub
    url(r'^hub/(?P<hubslug>[^\.]+)/(?P<rankby>[^\.]+)/(?P<timespan>[^\.]+)/$', views.stories,
        {'filterby': 'hub'}),    
    url(r'^hub/(?P<hubslug>[^\.]+)/(?P<rankby>[^\.]+)/$', views.stories,
        {'filterby': 'hub'}),    
    url(r'^hub/(?P<hubslug>[^\.]+)/$', views.stories,
        {'filterby': 'hub'}),

    # Frontpage(all)
    url(r'^(?P<rankby>[^\.]+)/(?P<timespan>[^\.]+)/$', views.stories),    
    url(r'^(?P<rankby>[^\.]+)/$', views.stories),    
    url(r'^$', views.stories),
    # url(r'^story/(?P<story>[^\.]+)/feed$', views.story_feed),
]
