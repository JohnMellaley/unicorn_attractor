from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile, statistics, getdata_bug, getdata_feature, getdata_bug_user, getdata_feature_user, bug_feature_count
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset)),
    url(r'^statistics/', statistics, name="statistics"),
    url(r'^getdata_bug/', getdata_bug, name="getdata_bug"),
    url(r'^getdata_feature/', getdata_feature, name="getdata_feature"),
    url(r'^getdata_bug_user/', getdata_bug_user, name="getdata_bug_user"),
    url(r'^getdata_feature_user/', getdata_feature_user, name="getdata_feature_user"),
    url(r'^bug_feature_count/', bug_feature_count, name="bug_feature_count"),
]