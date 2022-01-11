from rest_framework import serializers
from . import models
from course.models import Course
from rest_framework.exceptions import ValidationError


class OrderSerializer(serializers.ModelSerializer):
    """
    反序列化，前段传入的数据进行返序列化
    把 course:[1,2,3] 处理为 [object1,...]
    """
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), write_only=True,
                                                many=True)

    class Meta:
        model = models.Order
        fields = ['total_amount', 'subject', 'pay_type']

    def _check_price(self, attrs):
        total_amount = attrs.get('total_amount')
        course_list = attrs.get('course')
        total_price = None
        for course in course_list:
            total_price += course.price
        if total_price != total_amount:
            raise ValidationError('价格不合法')
        return total_amount

    @staticmethod
    def _gen_out_trade_no():
        import uuid
        return str(uuid.uuid4())

    def _get_user(self):
        request = self.context.get('request')
        return request.user

    def validate(self, attrs):
        # 1.订单价格校验
        # 2. 生成订单号
        # 3. 支付用户
        # 4.支付宝链接
        # 5.入库，入两个表
        total_amount = self._check_price(attrs)
        out_trade_no = self._gen_out_trade_no()
        user = self._get_user()
