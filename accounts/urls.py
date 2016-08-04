from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('^register/$', views.register, name="register"),
    url('^profile/$',views.user_profile,name="user_profile"),
    url('^', include('django.contrib.auth.urls')),
]
