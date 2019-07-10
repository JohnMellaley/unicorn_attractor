from django.conf.urls import url, include
from .views import all_bugs, create_an_bug, likes, viewbug, create_post

urlpatterns = [
    url(r'^$', all_bugs, name='bugs'),
    url(r'^add$', create_an_bug, name='add'),
    url(r'^likes$', likes, name='likes'),
    url(r'^viewbug/(?P<bugid>\d+)$', viewbug, name='viewbug'),
    url(r'^create_post/(?P<bugid>\d+)$', create_post, name='create_post')
    ]
    