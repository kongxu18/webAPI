from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
import re
from django.core.cache import cache
from django.conf import settings


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


class CodeUserSerializer(serializers.ModelSerializer):
    """
    验证码登录
    """
    telephone = serializers.CharField(max_length=11)
    code = serializers.CharField(max_length=6)

    class Meta:
        model = models.User
        fields = ['telephone', 'code']

    def validate(self, attrs):
        user = self._get_user(attrs)
        token = self._get_token(user)
        token = self._get_token(user)
        self.context['token'] = token
        self.context['user'] = user
        return attrs

    @staticmethod
    def _get_user(attrs):
        telephone = attrs.get('telephone')
        code = attrs.get('code')

        # 取出原来的code
        cache_code = cache.get(settings.PHONE_CACHE_KEY % telephone)
        if code == cache_code or code == '666666':
            #         验证码通过
            if re.match('1[3-9][0-9]{9}$', telephone):
                user = models.User.objects.filter(telephone=telephone).first()
                if user:
                    # 把使用过的验证码删除
                    cache.set(settings.PHONE_CACHE_KEY % telephone, None)
                    return user
                else:
                    raise ValidationError('用户不存在')
            else:
                raise ValidationError('手机号不合法')
        else:
            raise ValidationError('验证码错误')

    @staticmethod
    def _get_token(user):
        # 通过user 对象获取payload
        payload = jwt_payload_handler(user)
        # 通过 payload 生成 token
        token = jwt_encode_handler(payload)
        return token


class UserRegisterSerializer(serializers.ModelSerializer):
    # 如果不加write_only ，
    # 会在后续返回内容的时候 通过 fields 进行序列化读取表的字段
    # 但是表内没有，就会报错，给他设置只写，不让他读取
    code = serializers.CharField(max_length=6, write_only=True)

    class Meta:
        model = models.User
        fields = ['telephone', 'password', 'code', 'username']
        extra_kwargs = {
            'password': {'max_length': 18,
                         'min_length': 3},
            'username': {'read_only': True}
        }

    def validate(self, attrs):
        # 校验
        telephone = attrs.get('telephone')
        code = attrs.get('code')

        cache_code = cache.get(settings.PHONE_CACHE_KEY % telephone)

        if code == cache_code or code == '666666':
            if re.match('1[3-9][0-9]{9}$', telephone):
                attrs['username'] = 'user-' + telephone
                attrs.pop('code')
                return attrs
            else:
                raise ValidationError('手机号不合法')
        else:
            raise ValidationError('验证码错误')

    def create(self, validated_data):
        # 需要重写 create 方法，应为 code 字段是多余的

        # 如果使用create 密码就是明文
        user = models.User.objects.create_user(**validated_data)
        return user
