from celery_task import app
from celery.result import AsyncResult

id = 'f9804578-81b8-40bf-a20d-f63e03c84b28'

if __name__ == '__main__':
    async_ = AsyncResult(id=id, app=app)
    if async_.successful():
        result = async_.get()
        print(result)
    elif async_.failed():
        print(0)
    elif async_.status == 'PENDING':
        print('等待执行')
    elif async_.status == 'RETRY':
        print('重试')
    elif async_.status == 'started':
        print('已开始被执行')
