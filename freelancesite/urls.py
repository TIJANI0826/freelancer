from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'freelancesite'
urlpatterns = [
    path('home', views.index, name='index'),
    path('thanks', views.thanks, name ='thanks')
]