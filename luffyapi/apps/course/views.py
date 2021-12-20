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


class CourseView(GenericViewSet, ListModelMixin):
    queryset = models.Course.objects.filter(is_delete=False,
                                            is_show=True).order_by('orders')
    serializer_class = serializer.CourseModelSerializer
    # 分页
    pagination_class = PageNumberPagination
