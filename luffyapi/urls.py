"""luffyapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings

# xadmin 依赖
import xadmin

xadmin.autodiscover()
# xyersion 模块自动注册需要版本控制的model
from xadmin.plugins import xversion

xversion.register_models()

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('home/', include('home.urls')),
    path('user/', include('user.urls')),
    path('course/', include('course.urls')),
    path('order/', include('order.urls')),

    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
]
