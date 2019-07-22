from django.conf.urls import url, include
from .views import all_features, create_feature, create_post, viewfeature

urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^create_feature$', create_feature, name='create_feature'),
    url(r'^viewfeature/(?P<featureid>\d+)$', viewfeature, name='viewfeature'),
    url(r'^create_post/(?P<featureid>\d+)$', create_post, name='create_post')
]