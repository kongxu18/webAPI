"""
异步任务
"""
import os

import django
from celery import Celery

# 加载django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE','luffyapi.settings.dev')
django.setup()

# 任务中间件 存储任务
broker = 'redis://:333333@175.24.179.83:6379/1'

# backend 任务结果仓库
backend = 'redis://:333333@175.24.179.83:6379/2'

# 这里把任务文件进行注册
app = Celery(__name__, broker=broker, backend=backend
             , include=['celery_task.home_task'])

# 执行定时任务
# 时区
app.conf.timezone = 'Asia/Shanghai'
# 是否使用utc
app.conf.enable_utc = False

# 任务定时配置
from datetime import timedelta
from celery.schedules import crontab

# crontab(hour=8,day_of_week=1) 每周一早8点执行
app.conf.beat_schedule = {
    'add-task': {
        'task': 'celery_task.home_task.banner_update',
        'schedule': timedelta(seconds=30),
        # 'args': (300, 50)
    }
}
"""
之前的任务，都是需要代码去手动提交到worker
同样定时任务，其实就是按照设定的周期用beat自动提交

需要一个启动一个beat
用来定时提交任务到worker

启动beat：

celery -A celery_task beat -l info
"""
