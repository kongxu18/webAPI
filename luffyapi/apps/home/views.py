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


# class BannerView(GenericAPIView, ListModelMixin):
class BannerView(GenericViewSet, ListModelMixin):
    """
    轮播图视图
    """
    # 无论有多少数据就展示三条
    counter = settings.BANNER_COUNTER
    queryset = models.Banner.objects. \
        filter(is_delete=False, is_show=True).order_by('display_order')[:counter]
    serializer_class = serializer.BannerModelSerializer
