"""
首页轮播图的异步更新

由于celery 和 django 是2个独立的程序

启动work 和 beat 以后
定时任务读取 cache ，celery 读取不到django 的环境
需要设置进去 可以在celery 中配置

"""
from .celery import app
from django.core.cache import cache
from home import models, serializer
from django.conf import settings
from django.core.cache import cache
import time

"""
需要先加载django 环境
不然 cache 获取不到
"""
# cache
# serializer

@app.task
def banner_update():
    queryset_banner = models.Banner.objects.filter(is_delete=False,
                                                   is_show=True).order_by('orders')[:settings.BANNER_COUNTER]

    serializer_banner = serializer.BannerModelSerializer(instance=queryset_banner,
                                                         many=True)

    for banner in serializer_banner.data:
        banner['img'] = 'http://127.0.0.1:8000' + banner['img']

    cache.set('banner_list',serializer_banner.data)
    time.sleep(1)
    banner_list = cache.get('banner_list')
    print(banner_list)
    return True
