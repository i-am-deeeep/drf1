from django.urls import path
from drfApp import views

urlpatterns = [
    path("movie_list/",views.movie_list),
    path("movie/<int:pk>",views.movie)
]