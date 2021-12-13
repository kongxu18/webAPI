"""
添加celery任务
"""
from celery_task.task_1 import add

id  = add.delay(1, 2)
print(id)
from celery_task.task_2 import add

id2 = add.delay(2, 5)
print(id2)