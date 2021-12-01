from django.shortcuts import render

# Create your views here.
from user import models
from rest_framework.viewsets import ViewSet
from . import serializer
from luffyapi.utils.response import APIResponse
from rest_framework.decorators import action
import re


class LoginView(ViewSet):
    """
    多方式登录接口
    手机号验证是否存在接口
    """

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

    @action(methods=['GET'], detail=False)
    def check_telephone(self, request, *args, **kwargs):
        telephone = request.query_params.get('telephone')
        if not re.match('^1[3-9][0-9]{9}$', telephone):
            return APIResponse(code=0, msg='手机号不合法')
        try:
            user = models.User.objects.filter(telephone=telephone)
            if user:
                return APIResponse(code=1, msg='存在手机号')
            else:
                return APIResponse(code=0, msg='手机号不存在')
        except:
            return APIResponse(code=0, msg='手机号不存在')
