from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name='index'),
    path("movies/", views.Movies, name='movie'),
    path("sports/", views.Sports, name='sport'),
    path("politics/", views.Politics, name='politics'),
]

