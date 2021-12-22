from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from . import models, serializer


class CourseCategoryView(GenericViewSet, ListModelMixin):
    """
    课程分类群查接口
    """
    queryset = models.CourseCategory.objects.filter(is_delete=False,
                                                    is_show=True).order_by('orders')
    serializer_class = serializer.CourseCategorySerializer


from .paginations import PageNumberPagination

"""
原生的过滤 只能过滤当前表的字段，对于表的外键关联字段没法进行过滤
所以使用第三方的filter：django-filter
"""
from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters.rest_framework import DjangoFilterBackend


class CourseView(GenericViewSet, ListModelMixin):
    queryset = models.Course.objects.filter(is_delete=False,
                                            is_show=True).order_by('orders')
    serializer_class = serializer.CourseModelSerializer
    # 分页
    pagination_class = PageNumberPagination

    # 排序，过滤
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # , SearchFilter]
    #     排序
    ordering_fields = ['id', 'price', 'students']

    # 配置过滤的字段
    # search_fields = ['id']

    # 使用的扩展django-filter 配置的搜索字段
    filter_fields = ['course_category']
