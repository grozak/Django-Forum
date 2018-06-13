from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #/forum/
    re_path(r'^$', views.index, name='index'),
    #/forum/10
    re_path(r'^(?P<thread_id>[0-9]+)/$', views.thread, name='thread'),
    #/forum/register
    re_path(r'^register/$', views.register, name='register'),
    #forum/login
    re_path(r'^login/$', auth_views.login, name='login'),
    re_path(r'^logout/$', auth_views.logout, {'next_page': '/forum'}, name='logout'),
]
