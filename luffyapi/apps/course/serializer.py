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
                  'signature', 'image', 'brief']


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
                  'attachment_path', 'pub_sections', 'price',
                  'students', 'period', 'sections', 'level',
                  'teacher', 'course_type_name', 'level_name',
                  'status_name', 'section_list']


class CourseSectionSerializer(ModelSerializer):
    """
    课时
    """
    class Meta:
        model = models.CourseSection
        fields = ['name', 'orders', 'duration', 'free_trail', 'section_link', 'section_type_name']


class CourseChapterSerializer(ModelSerializer):
    # 一个章节 有多个课时 需要many
    coursesections = CourseSectionSerializer(many=True)

    class Meta:
        model = models.CourseChapter
        fields = ['name', 'summary', 'chapter', 'coursesections']
