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
        fields = ['name', 'title', 'role_name',
                  'signature','image','brief']


class CourseModelSerializer(ModelSerializer):
    """
    课程群查
    """

    # 一对多关系，一个老师多个课程
    # 子序列化
    teacher = TeacherSerializer(many=False)

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'course_img', 'brief',
                  'attachment_path','pub_sections','price',
                  'students','period','sections','level',
                  'teacher', 'course_type_name', 'level_name',
                  'status_name', 'section_list']
