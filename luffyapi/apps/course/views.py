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
"""
from rest_framework.filters import OrderingFilter, SearchFilter


class CourseView(GenericViewSet, ListModelMixin):
    queryset = models.Course.objects.filter(is_delete=False,
                                            is_show=True).order_by('orders')
    serializer_class = serializer.CourseModelSerializer
    # 分页
    pagination_class = PageNumberPagination

    # 排序，过滤
    filter_backends = [OrderingFilter, SearchFilter]
    #     排序
    ordering_fields = ['id', 'price']

    # 配置过滤的字段
    search_fields = ['id']
