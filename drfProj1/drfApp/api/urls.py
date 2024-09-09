from django.urls import path
from drfApp.api import views

# urlpatterns = [
#     path("movie_list/",views.movie_list),
#     path("movie/<int:pk>",views.movie)
# ]

urlpatterns = [
    path("movie_list/",views.Movie_list_AV.as_view()),
    path("movie/<int:pk>",views.Movie_AV.as_view())
]