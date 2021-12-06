import os
from pathlib import Path
import sys, os

# Build paths :D:\PythonProjects\djangoProject\luffyapi\luffyapi ---
BASE_DIR = Path(__file__).resolve().parent.parent
# 把这个路径加入环境变量
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(1, str(Path(BASE_DIR) / 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b03ybb3fi4!20!%vu-*cg$&b7qr+sp@x$az#-l!(e22n73ch*w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',

    'xadmin',  # xadmin
    'crispy_forms',  # 渲染表格模块
    'reversion',  # 模型的版本控制，可以回滚数据

    'user',  # 应为apps 目录已经被加入环境变量，所以可以直接能找到
    'home',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 自己写的跨域资源共享
    # 'luffyapi.utils.middle.MyMiddle',
    # 别人写好的cors 跨域资源共享
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'luffyapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'luffyapi.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'luffyapi',
        'USER': 'luffyapi',
        'PASSWORD': '333333',
        'PORT': 3306,
        'HOST': '175.24.179.83'
    }
}
# import pymysql
# pymysql.install_as_MySQLdb()
"""
安装了mysqlclient 直接就成了
"""
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 配置 使用django user表
AUTH_USER_MODEL = 'user.user'

# 配置 media 图标
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / Path('media')

# 日志的配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            # 实际开发建议使用WARNING
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            # 实际开发建议使用ERROR
            'level': 'INFO',
            # 到达300M 就会新建一个
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置,日志文件名,日志保存目录必须手动创建，注：这里的文件路径要注意BASE_DIR代表的是小luffyapi
            'filename': str(BASE_DIR.parent / 'logs' / 'luffy.log'),
            # 日志文件的最大值,这里我们设置300M
            'maxBytes': 300 * 1024 * 1024,
            # 日志文件的数量,设置最大日志数量为10
            'backupCount': 10,
            # 日志格式:详细格式
            'formatter': 'verbose',
            # 文件内容编码
            'encoding': 'utf-8'
        },
    },
    # 日志对象
    'loggers': {
        # logging.getLogger() 括号内的名字就是下面的key django
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,  # 是否让日志信息继续冒泡给其他的日志处理系统
        },
    }
}
# 封装一个log对象

# 配置  django-cors-headers
# 跨域资源共享
CORS_ALLOW_CREDENTIALS = True  # 允许发送cookie
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = ('*')
# CORS_ALLOW_HEADERS 有自带的默认配置
# CORS_ALLOW_METHODS 有自带的默认配置


# restframework 配置
REST_FRAMEWORK = {
    # 捕获所有出现的错误
    'EXCEPTION_HANDLER': 'luffyapi.utils.exceptions.common_exception_handler',
    # 手机频率限制配置
    'DEFAULT_THROTTLE_RATES': {
        'sms': '1/m'
    }
}

from .const import *

"""
jwt 过期时间
"""
import datetime

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    # 'JWT_RESPONSE_PAYLOAD_HANDLER':''
}

# 手机验证码缓存的key值
PHONE_CACHE_KEY = 'sms_cache_%s'
