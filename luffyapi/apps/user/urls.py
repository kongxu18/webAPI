from django.urls import re_path, path
from . import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', views.LoginView, 'login')

urlpatterns = [

]

urlpatterns += router.urls
