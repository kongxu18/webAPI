from rest_framework import serializers
from . import models
from course.models import Course
from rest_framework.exceptions import ValidationError
from django.conf import settings


class OrderSerializer(serializers.ModelSerializer):
    """
    反序列化，前段传入的数据进行返序列化
    把 course:[1,2,3] 处理为 [object1,...]
    """
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), write_only=True,
                                                many=True)

    class Meta:
        model = models.Order
        fields = ['total_amount', 'subject', 'pay_type', 'course']
        extra_kwargs = {
            'total_amount': {'required': True},
            'pay_type': {'required': True},
        }

    def _check_price(self, attrs):
        total_amount = attrs.get('total_amount')
        course_list = attrs.get('course')
        total_price = 0
        for course in course_list:

            try:
                total_price += course.price
            except Exception as err:
                print(err)
        if total_price != total_amount:
            raise ValidationError('价格不合法')
        return total_amount

    @staticmethod
    def _gen_out_trade_no():
        import uuid
        return str(uuid.uuid4())

    def _get_user(self):
        # 需要request对象 可以通过视图函数传入
        request = self.context.get('request')
        return request.user

    def _gen_pay_url(self, out_trade_no, total_amount, subject):
        # total_amount 是decimal 类型，识别不了，需要转float
        from luffyapi.libs.al_pay import alipay, gateway

        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=out_trade_no,
            total_amount=float(total_amount),
            subject=subject,
            return_url=settings.RETURN_URL,  # get 支付宝同步回调
            notify_url=settings.NOTIFY_URL  # post 支付宝异步回调
        )

        return gateway + order_string

    def _before_create(self, attrs, user, pay_url, out_trade_no):
        attrs['user'] = user
        attrs['out_trade_no'] = out_trade_no
        # context 用于序列化器和view 交互数据
        self.context['pay_url'] = pay_url

    def validate(self, attrs):
        # 1.订单价格校验
        # 2. 生成订单号
        # 3. 支付用户
        # 4.支付宝链接
        # 5.入库，入两个表
        total_amount = self._check_price(attrs)
        out_trade_no = self._gen_out_trade_no()
        subject = attrs.get('subject')
        user = self._get_user()

        pay_url = self._gen_pay_url(out_trade_no, total_amount, subject)
        self._before_create(attrs, user, pay_url, out_trade_no)
        return attrs

    def create(self, validated_data):
        course_list = validated_data.pop('course')
        # 主订单
        order = models.Order.objects.create(**validated_data)
        # 子订单
        for course in course_list:
            models.OrderDetail.objects.create(order=order, course=course, price=course.price,
                                              real_price=course.price)
        return order
