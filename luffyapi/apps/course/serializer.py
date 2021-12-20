from rest_framework.serializers import ModelSerializer
from . import models


class CourseCategorySerializer(ModelSerializer):
    """
    课程类型
    """

    class Meta:
        model = models.CourseCategory
        fields = ['id', 'name']


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['name', 'title', 'role_name']


class CourseModelSerializer(ModelSerializer):
    """
    课程群查
    """

    # 一对多关系，一个老师多个课程
    # 子序列化
    teacher = TeacherSerializer()

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'course_img', 'brief', 'level',
                  'teacher', 'course_type_name', 'level_name',
                  'status_name', 'course_sections']
