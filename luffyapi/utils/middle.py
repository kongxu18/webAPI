"""
中间件
自己处理跨域问题
允许跨域
简单请求
非简单请求 处理options 请求
"""
from django.utils.deprecation import MiddlewareMixin
from django.middleware.csrf import CsrfViewMiddleware


class MyMiddle(MiddlewareMixin):
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        if request.method == 'OPTIONS':
            response['Access-Control-Allow-Origin'] = 'Content-Type'
        return response

"""
别人写好的跨域处理
django-cors-headers
"""