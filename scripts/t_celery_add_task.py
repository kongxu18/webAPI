"""
添加celery任务
"""
from celery_task.task_1 import add
"""
执行异步任务
"""
id = add.delay(1, 2)
print(id)
from celery_task.task_2 import add

id2 = add.delay(2, 5)
print(id2)

"""
执行延迟任务
"""
from celery_task.task_1 import add
from datetime import datetime, timedelta

# 表示十秒之后的时间
eta = datetime.utcnow() + timedelta(seconds=10)

# args 函数的参数，eta 延迟时间，utc时间
add.apply_async(args=(200,5),eta=eta)


"""
执行定时任务
在 主py里配置
"""