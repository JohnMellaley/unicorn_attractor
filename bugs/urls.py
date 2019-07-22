from django.conf.urls import url, include
from .views import all_bugs, create_an_bug, likes, viewbug, create_post_bug

urlpatterns = [
    url(r'^$', all_bugs, name='bugs'),
    url(r'^add$', create_an_bug, name='add'),
    url(r'^likes$', likes, name='likes'),
    url(r'^viewbug/(?P<bugid>\d+)$', viewbug, name='viewbug'),
    url(r'^create_post_bug/(?P<bugid>\d+)$', create_post_bug, name='create_post_bug')
    ]
    