from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('myStatsheets', views.myStatsheets),
path('statsheetDetail', views.statsheetDetail),
path("accounts/", include("django.contrib.auth.urls")),
path('accounts/register/', views.registerPage, name = 'register_page'),

]
