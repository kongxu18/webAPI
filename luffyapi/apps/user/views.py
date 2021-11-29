from django.shortcuts import render

# Create your views here.
from user import models
from rest_framework.viewsets import ViewSet
from . import serializer
from luffyapi.utils.response import APIResponse
from rest_framework.decorators import action


class LoginView(ViewSet):
    # 自动加装路由
    @action(methods=['POST'], detail=False)
    def login(self, request, *args, **kwargs):
        ser = serializer.UserSerializer(data=request.data)
        if ser.is_valid():
            token = ser.context['token']
            username = ser.context['user'].username

            return APIResponse(token=token, username=username)
        else:
            return APIResponse(code=0, msg=ser.errors)
