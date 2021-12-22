from rest_framework.filters import BaseFilterBackend

"""
自己定义的过滤类
只需要重写 filter_queryset 方法
"""


class MyFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # 正真的过滤规则
        # params = queryset.Get.get('xxx')
        # queryset.filter('''''')
        return queryset[:1]
