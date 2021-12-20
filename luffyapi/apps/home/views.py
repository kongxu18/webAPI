from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from luffyapi.utils.response import APIResponse


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        dic = {}
        print(dic['name'])

        # 跨域资源共享 在响应头加上以下key，允许该源的访问
        return APIResponse(headers={'Access-Control-Allow-Origin':
                                        '127.0.0.1:8008'})


from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from . import models
from . import serializer
from django.conf import settings
from rest_framework.response import Response
from django.core.cache import cache

# class BannerView(GenericAPIView, ListModelMixin):
class BannerView(GenericViewSet, ListModelMixin):
    """
    轮播图视图
    """
    # 无论有多少数据就展示三条
    counter = settings.BANNER_COUNTER
    queryset = models.Banner.objects. \
        filter(is_delete=False, is_show=True).order_by('orders')[:counter]
    serializer_class = serializer.BannerModelSerializer

    def list(self, request, *args, **kwargs):
        """
        对首页轮播图信息进行缓存
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        # 首先拿数据
        banner_list = cache.get('banner_list')
        if not banner_list:
            # 从数据库拿
            response = super().list(request, *args, **kwargs)
            # 加到缓存
            cache.set('banner_list',response.data,60*60*24*7)
            return response
        return Response(data=banner_list)
