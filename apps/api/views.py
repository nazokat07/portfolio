from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework import generics

from apps.main.models import *

from .serializers import UsersSerializer
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
    















