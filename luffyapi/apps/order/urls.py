from django.urls import re_path, path, include
from . import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('pay', views.PayView, 'pay')
urlpatterns = [
    path('', include(router.urls)),
]
