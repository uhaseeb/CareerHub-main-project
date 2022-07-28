from ast import pattern
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.post , name='post'),
    path('signup', views.signup, name='signup'),
    path('create_user', views.create_user, name='create_user'),
    path('login', views.login, name='login'),
    path('login_auth', views.login_auth, name='login_auth'),
    path('studentdashboard', views.studentdashboard, name='studentdashboard'),
    path('studentprofile', views.studentprofile, name='studentprofile')
 ]