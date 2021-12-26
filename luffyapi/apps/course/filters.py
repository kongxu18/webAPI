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


from django_filters.filterset import FilterSet
from . import models

from django_filters import filters


class CourseFilterSet(FilterSet):
    # 实现区间过滤
    # 意思是 price 大于 min 小于max
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gt')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = models.Course
        fields = ['course_category']
