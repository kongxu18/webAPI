"""
异步任务
"""
from celery import Celery

# 任务中间件 存储任务
broker = 'redis://:333333@175.24.179.83:6379/1'

# backend 任务结果仓库
backend = 'redis://:333333@175.24.179.83:6379/2'

# 这里把任务文件进行注册
app = Celery(__name__, broker=broker, backend=backend
             ,include=['celery_task.task_1','celery_task.task_2'])
