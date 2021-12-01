from qcloudsms_py import SmsSingleSender
from luffyapi.utils.logger import log
from . import settings


# 生成一个四位随机验证码
def get_code():
    import random
    s_code=''
    for i in range(4):
        s_code+=str(random.randint(0,9))
    return s_code


def send_message(phone,code):

    ssender = SmsSingleSender(settings.appid, settings.appkey)
    params = [code, '3']  # 当模板没有参数时，`params = []`
    try:
        result = ssender.send_with_param(86, phone, settings.template_id, params, sign=settings.sms_sign, extend="", ext="")
        if result.get('result') == 0:
            return True
        else:
            return code
    except Exception as e:
        log.error('手机号：%s,短信发送失败,错误为：%s'%(phone,str(e)))
        return code
