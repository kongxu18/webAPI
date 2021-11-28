from django.urls import re_path, path, include
from . import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('banner', views.BannerView, 'banner')
urlpatterns = [
    path('', views.TestView.as_view()),
    path('', include(router.urls))
]
