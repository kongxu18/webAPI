from django.shortcuts import render

# Create your views here.
from user import models
from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin
from . import serializer
from luffyapi.utils.response import APIResponse
from rest_framework.decorators import action
import re

from luffyapi.libs.tx_sms import get_code, send_message
from django.core.cache import cache
from django.conf import settings

from .throttlings import SMSThrottling


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

    @action(methods=['POST'], detail=False)
    def code_login(self, request, *args, **kwargs):
        """
        验证码登录
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ser = serializer.CodeUserSerializer(data=request.data)
        if ser.is_valid():
            token = ser.context['token']
            username = ser.context['user'].username
            return APIResponse(token=token, username=username)
        else:
            return APIResponse(code=0, msg=ser.errors)


class SendSmsView(ViewSet):
    throttle_classes = [SMSThrottling]

    @action(methods=['GET'], detail=False)
    def send(self, request, *args, **kwargs):
        """
        发送验证码接口
        :return:
        """
        telephone = request.query_params.get('telephone')
        if not re.match('^1[3-9][0-9]{9}$', telephone):
            SMSThrottling.is_send = False

            return APIResponse(code=0, msg='手机号不合法')

        code = get_code()
        result = send_message(telephone, code)
        # sms_cahce_%s
        cache.set(settings.PHONE_CACHE_KEY % telephone, code, 180)

        # 使用redis conn
        conn = self.cache_redis()
        conn.set(settings.PHONE_CACHE_KEY % telephone, code, 180)
        if result == True:
            return APIResponse(code=1, msg='验证码发送成功')
        else:
            SMSThrottling.is_send = False
            return APIResponse(code=0, msg='验证码发送失败', result=result)

    def cache_redis(self):
        # 使用redis 连接操作缓存
        from django_redis import get_redis_connection
        return get_redis_connection('default')


class RegisterView(GenericViewSet, CreateModelMixin):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        # 重写父类的create ，更改返回的东西
        response = super().create(request, *args, **kwargs)
        username = response.data.get('username')
        return APIResponse(code=1, msg='注册成功', username=username)
