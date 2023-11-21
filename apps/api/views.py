from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework import generics

from apps.main.models import *

from .api import get_weather_data
from .serializers import UsersSerializer
from .serializers import PostsSerializer
from .serializers import PostSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class UsersAPIView(APIView):

    def get(self, request):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = UsersSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

class UsersDetailAPIView(APIView):

    def get(self, request, pk):
        users = Users.objects.get(pk=pk)
        serializer = UsersSerializer(Users)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request, pk):
        users = Users.objects.get(pk=pk)
        serializer = UsersSerializer(Users, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        users = Users.objects.get(pk=pk)
        users.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    









class PostsAPIView(APIView):

    def get(self, request):
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = PostsSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

class PostsDetailAPIView(APIView):

    def get(self, request, pk):
        posts = Posts.objects.get(pk=pk)
        serializer = PostsSerializer(Posts)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request, pk):
        posts = Posts.objects.get(pk=pk)
        serializer = PostsSerializer(Posts, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        posts = Posts.objects.get(pk=pk)
        posts.delete()
        return Response(status=HTTP_204_NO_CONTENT)




def weather_view(request):
    city = 'Nukus'  # Замените на желаемый город
    weather_data = get_weather_data(city)

#  return render(request, 'weather_app/weather.html', {'weather_data': weather_data})

