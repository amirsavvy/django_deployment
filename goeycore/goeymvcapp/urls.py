from goeymvcapp import views
from django.conf.urls import url

app_name = 'goeymvcapp'

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^register/$', views.get_registeration, name='get_register'),
    url(r'^register-done/$', views.post_registeration, name='post_register'),
    url(r'^login/$', views.get_login, name='get_login'),
    url(r'^login-done/$', views.post_login, name='post_login'),

]
