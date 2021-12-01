from rest_framework.views import exception_handler
from .response import APIResponse
from .logger import log


def common_exception_handler(exc, contest):
    """
    contest['view'] 是 TestView 对象，想拿出这个对象的类名
    """
    log.error('出错视图view:%s,错误是%s' % (contest['view'].__class__.__name__, str(exc)))
    # print(exc,type(exc))
    ret = exception_handler(exc, contest)
    if not ret:
        """
        drf 内置处理不了，丢给django
        自己处理
        """
        # 可以添加更具体的异常
        if isinstance(exc, KeyError):
            return APIResponse(code=0, msg='err', result='key error')
        return APIResponse(code=0, msg='error', result=str(exc))
    else:
        return APIResponse(code=0, msg='err', result=ret.data)
