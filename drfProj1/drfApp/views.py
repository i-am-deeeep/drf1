from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from drfApp.models import Movie
# Create your views here.
def movie_list(request):
    movies=Movie.objects.all()
    data={"movie":list(movies.values())}
    return JsonResponse(data)

def movie(request,pk):
    movie=Movie.objects.get(pk=pk)
    data={
        "name":movie.name,
        "rating":movie.rating,
        "description":movie.description
    }
    return JsonResponse(data)
