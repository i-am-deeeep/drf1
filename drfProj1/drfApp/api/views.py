from drfApp.models import Movie
from drfApp.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view

from rest_framework.views import APIView

class Movie_list_AV(APIView):
    def get(self,request):
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):    #(raise_exception=True) gives status code 400
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class Movie_AV(APIView):
    def get(self,request,pk):
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movie,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        movie=Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method=='GET':
#         movies=Movie.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         return Response(serializer.data)
#     if request.method=='POST':
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def movie(request,pk):
#     try:
#         movie=Movie.objects.get(pk=pk)
#     except:
#         return Response({"error":"movie not found"},status=status.HTTP_404_NOT_FOUND)

#     if request.method=='GET':
#         serializer=MovieSerializer(movie,many=False)
#         return Response(serializer.data)
#     if request.method=='PUT':
#         serializer=MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     if request.method=='DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
