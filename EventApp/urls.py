from django.urls import path
from . import views

urlpatterns = [
  path("home/", views.home, name="home"),
  path("events/", views.events, name="events"),
  #path("/reloadevents", 
       #views.reloadevents, 
       #name="reloadevents")
]