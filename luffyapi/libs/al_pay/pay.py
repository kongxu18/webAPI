from alipay import AliPay
from . import setting

app_private_key_string = setting.APP_PRIVATE_KEY_STRING
alipay_public_key_string = setting.ALIPAY_PUBLIC_KEY_STRING

alipay = AliPay(
    appid=setting.APPID,
    app_notify_url=None,  # 默认回调 url
    app_private_key_string=app_private_key_string,
    # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    alipay_public_key_string=alipay_public_key_string,
    sign_type=setting.SIGN_TYPE,  # RSA 或者 RSA2
    debug=setting.DEBUG,  # 默认 False
    verbose=False,  # 输出调试数据
    # config=AliPayConfig(timeout=15)  # 可选，请求超时时间
)

gateway = setting.GATEWAY