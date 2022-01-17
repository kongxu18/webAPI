from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from . import models, serializer
from rest_framework.response import Response

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView


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


class SuccessView(APIView):
    """
    支付宝回调 post
    前端回调 get
    """

    def get(self, request, *args, **kwargs):
        out_trade_no = request.query_params.get('out_trade_no')
        order = models.Order.objects.filter(out_trade_no=out_trade_no).first()
        if order.order_status == 1:
            return Response(True)
        elif order.order_status == 0:
            return Response(False)
        return Response('后台收到')

    def post(self, request, *args, **kwargs):
        """
        支付宝回调接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        from luffyapi.utils.logger import log
        from luffyapi.libs.al_pay import alipay
        data = request.data.dict()
        out_trade_no = data.get('out_trade_no', None)
        gmt_payment = data.get('gmt_payment', None)
        signature = data.pop('sign')
        # 验证签名

        success = alipay.verify(data, signature)

        if success and data['trade_status'] in ('TRADE_SUCCESS', 'TRADE_FINISHED'):
            models.Order.objects.filter(out_trade_no=out_trade_no).update(order_status=1, pay_time=gmt_payment)
            log.info('%s订单支付成功' % out_trade_no)
            return Response('success')
        else:
            log.info('%s订单支付失败' % out_trade_no)
            return Response('error')
