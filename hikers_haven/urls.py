from django.urls import path

from . import views

#the paths to URLs will go here
urlpatterns = [
    path('', views.index, name='index'),
]
