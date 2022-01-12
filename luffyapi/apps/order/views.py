from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from . import models, serializer
from rest_framework.response import Response

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

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
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Order.objects.all()
    serializer_class = serializer.OrderSerializer

    def create(self, request, *args, **kwargs):
        # context = {'request':request}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.context.get('pay_url'), status=201)
