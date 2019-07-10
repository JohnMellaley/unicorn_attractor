from django.conf.urls import url, include
from .views import all_features, create_feature

urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^create_feature$', create_feature, name='create_feature'),
]