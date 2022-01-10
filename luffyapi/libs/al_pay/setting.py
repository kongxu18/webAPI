import os

APPID = "2021000118685360"

APP_PRIVATE_KEY_STRING = \
    open(os.path.join(os.path.dirname(__file__), 'pem', 'private_key.pem'))
ALIPAY_PUBLIC_KEY_STRING = \
    open(os.path.join(os.path.dirname(__file__), 'pem', 'al_public_key.pem'))

SIGN_TYPE = "RSA2",  # RSA 或者 RSA2
DEBUG = False,  # 默认 False
VERBOSE = False,  # 输出调试数据

GATEWAY = 'https://openapi.alipaydev.com/gateway.do?' if DEBUG else 'https://openapi.alipay.com/gateway.do?'
