from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name= "index"),
    path("lewis", views.lewis, name = "lewis"),
    path("gimp", views.gimp, name = "gimp"),
    #path("<str:name>", views.greet, name = "greet"),
    path("<str:name>", views.greet1, name = "greet1")
]