from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
   # path("<str:title>", views.entry, name = "entry"),
    path("wiki/<str:title>",views.entry, name = "entry" )
   # path("<str:entry>", views.entry)
   # path("error", views.error, name = "error")
]
