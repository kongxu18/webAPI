"""
这里放任务 task
"""
from .celery import app

@app.task
def add(x,y):
    return x-y