from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile, statistics, getdata, dashboard_data_view
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset)),
    url(r'^statistics/', statistics, name="statistics"),
    url(r'^getdata', getdata, name="getdata"),
    url(r'^dashboard_data_view', dashboard_data_view, name="dashboard_data_view"),
    
]