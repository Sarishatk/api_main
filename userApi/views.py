from django.shortcuts import render
from userApi.serializers import UserRegisterSerializer
from rest_framework.views import APIView
from rest_framework import status
from userApi.models import *
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# Create your views here.


class UserRegisterView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        # vanna data ne edthu

        user_serialzer = UserRegisterSerializer(data = request.data)

        if user_serialzer.is_valid():

            user_serialzer.save()

            
