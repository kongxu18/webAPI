"""
异步任务
"""
from celery import Celery

# 任务中间件 存储任务
broker = 'redis://:333333@175.24.179.83:6379/1'

# backend 任务结果仓库
backend = 'redis://:333333@175.24.179.83:6379/2'

app = Celery(__name__, broker=broker, backend=backend)


# 添加任务
@app.task
def add(x, y):
    return x + y

# 使用命令执行
# linux
# celery  -A celery_task worker -l info

# windows
# pip3 install eventlet
# celery -A celery_task worker -l info -P eventlet
