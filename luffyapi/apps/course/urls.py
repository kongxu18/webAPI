from django.urls import re_path, path
from . import views

from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('categories', views.CourseCategoryView)
router.register('free',views.CourseView)
router.register('chapters',views.CourseChapterView)
urlpatterns = [

]

urlpatterns += router.urls
