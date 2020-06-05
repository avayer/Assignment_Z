from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .models import Activity_peroid
from .serializers import UserSerializer
from .serializers import Activity_peroidSerializer

class userList(APIView):

    def get(self, second_param):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True) 
        return Response(serializer.data)

    def post(self):
        pass


