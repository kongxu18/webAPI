from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = models.User
        fields = ['username', 'password', 'id']
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        user = self._get_user(attrs)
        token = self._get_token(user)

        # 放入context 中，可以在视图类里取出来
        self.context['token'] = token
        self.context['user'] = user
        return attrs


    @staticmethod
    def _get_user(attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        # 多种登录方式
        import re
        if re.match('1[3-9][0-9]{9}$', username):
            user = models.User.objects.filter(telephone=username).first()
        elif re.match('^.*@.*', username):
            user = models.User.objects.filter(email=username).first()
        else:
            user = models.User.objects.filter(username=username).first()
        if user:
            # 校验密码
            ret = user.check_password(password)
            if ret:
                return user
            else:
                raise ValidationError('密码错误')
        else:
            raise ValidationError('用户不存在')

    @staticmethod
    def _get_token(user):
        # 通过user 对象获取payload
        payload = jwt_payload_handler(user)
        # 通过 payload 生成 token
        token = jwt_encode_handler(payload)
        return token
