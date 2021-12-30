from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
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

from .filters import CourseFilterSet


class CourseView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
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

    """
    django-filter 过滤有2种方式
    1.配置类，配置字段filter_fields
    2.配置类，配置字段filter_class 可支持区间过滤
    """

    # 使用的扩展django-filter 配置的搜索字段
    # filter_fields = ['course_category']

    # 使用自定制的filter 进行区间过滤
    filter_class = CourseFilterSet


class CourseChapterView(GenericViewSet, ListModelMixin):
    """
    章节接口
    """
    queryset = models.CourseChapter.objects.filter(is_delete=False, is_show=True)
    serializer_class = serializer.CourseChapterSerializer

    # 查出来所有章节，需要根据 course 对章节进行过滤
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['course']


class CourseSearchView(GenericViewSet,ListModelMixin):
    """
    查询课程接口 根据name 查询
    """
    queryset = models.Course.objects.filter(is_delete=False,
                                            is_show=True).order_by('orders')
    serializer_class = serializer.CourseModelSerializer
    # 分页
    pagination_class = PageNumberPagination

    # 排序，过滤
    filter_backends = [SearchFilter]

    # 配置过滤的字段
    search_fields = ['name']