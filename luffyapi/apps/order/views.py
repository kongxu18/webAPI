from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from . import models, serializer
from rest_framework.response import Response


# Create your views here.
class PayView(GenericViewSet, CreateModelMixin):
    """
    订单支付接口：
    1.生成主订单，生成子订单 uuid
    2.验证登录 jwt
    3.当前用户 就是下单用户
    4.前后端的订单价格验证，是否计算后相同
    要往order，orderdetail 同时插入，需要重写create
    """
    queryset = models.Order.objects.all()
    serializer_class = serializer.OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)