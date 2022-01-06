from alipay import AliPay

app_private_key_string = """-----BEGIN PUBLIC KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCAchk6wvnWfyLBk6P0zs7/QrZSwL3pPwm4+qVwC75JBIVyWu4mLzr6RpeyAwE5GubrliVYEmuN4jjSRJNePahrL3gKvhlRgyrZsSIL0QildZGshCQfShatTKmeKn8OZIXzTu2fkvxKgl9fKz7T/L38CiUq+2ghbjBb9+eT+kRAoJ6/OrL+AOCXLLdNTV/kc8FjUh9XtAonsrVgNDlX7G0WQWZGSROq7E9PB+3hyOanU8hgTxso4DYpxq98fC4zo9GPznDzxUaGjmQ17EZVeKgXpOqfy8U/YEFuR3wBRmKUFcrXALSnOwn7TOcgbqevtH6xqvl8guRcKrVU+QaA73frAgMBAAECggEAQlouvFNCetLcYoFhXjKDbgvJYcBdmqNM43jfg50dZFzojuV4RtN5NRbIgFXbCOPjzGmYywFg/D+TuNNiCXnyicRQz8PaEmie9yvw+Ye3Xrn4UdVFT8CXLFkA+krbrdSx+bmZOSjWGat1lxUg9KOIhS28e5K5/SMN6kSLJb9QCM3yjdlEzzoSlBkJ/JOfmT66XKerZRfkWgyRhSB+eudC68KBZ3vRsQQ4DzS0oMSqSKoju/wCLqERNJ9OwpJBvnKEykCTaA39KVYYbyTqoWLjInO9icnoK/UJt9XN/i5ZycpiNnUypsow1wQq4zcBwikwvR/88eBJnOBBMYv+J0oI+QKBgQDWqiN49aEFq7SFbalWAFcWoPFqBSaNtTKn1/7gA9PTyzsKgYY8BQN79vSissuUAE5GW9x1F/MQ0mOCXRlBZCXZEYAbo+abtrgGqTqD+7pEfuApb+zVFO9QX+pF0ZUtpnAyojSyDz9GlKt8T9R6ixYXatUvwSNeVG19nzCVAqjRVwKBgQCZLc+mjc0CWkIe6W+ij910W5l1SsjhLTSshpze/EMFYwemeGbafCWollMhZtxFPEz0ei9Rg64iw+LC4deJ4EEY9wKPeLUTk4Is9s/i9EMnGdT5duTnk6cMOeKT9WOjtJ+B5Jo3PPE3spo8AVpi6akv5nisVz1owf+6vXL39ctNjQKBgQDNgnkPVmjf2vCqRMA3G4BEo7Q7gc7VH8HtOjZCFKf5Pbm6ZyIx18LsLRMrp+yKNni5lzxJxbHoSuMFbUe+eLhbRgvVamZecOFhTyY8MQS0iprkUMj1fmNWGV1ZljoxSARmFTBJv5seYTqDepG69+kgZiDO5SKNLlrcR0jlf3RLZQKBgEWhVHYymVGLc+kXVh7AZPuCtARkZWIuqXYPjvmyFEk7lfuvWZnRu1CiXNGfL1vtqFGtxRq50AuPneHWxaKwJQdTKX/McAuhDxifbSqOvIPmszBfQnieXt4o5f06G/wLnEJwh0W61y/paUEDoHG8I6NZkdtNoOWg4j2h5sQeoDb1AoGBAM+3LPQUDWIyLeoZAtZJMoRApFBVJmUirwihAGjC/n/G50VMIMFTilG6569jijp5C/ij2jZmsIfx3qWMlNweGcVx+LTJhEUFIdHhY/oasaDobNHPpX0ioODmBkMG/9jT6WgcOABWRDJTTJrCgYy2FFpwSyz0m13DdN99Er0luNsh
-----END PUBLIC KEY-----"""
alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2KGoAQJ57+WOB3YijkS6c4glfJjCaagRc4Ocmnmn7OVU/aEMmQVEuCg6Brw2cYicufXhkV4fgw9id5QmPgLwEj26d9tvzqLCJgIFfcYt0UR/qKDbtAA2j6dHm5aNX4yDQDOJv/glQ1gKWVJK3r6jaY7610JlSkkBhfZKYpb0N2ae/2nrMugR+BMyglbektaUiy9EGD8Ey0oz50w++xpJQZxGd7NQwwA7X11W4b3j4BLadJBAFGRfJVlvDNBTGUrI36biIulULrfMVOC1mIw3wFn/kpSEhNrKBo1KO0cP/9GeHNOq3rQ2XPfB94l6rAe3MZ/B0wSJMYZwCGmllOK3QQIDAQAB
-----END PUBLIC KEY-----"""

alipay = AliPay(
    appid="2021000118685360",
    app_notify_url=None,  # 默认回调 url
    app_private_key_string=app_private_key_string,
    # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    alipay_public_key_string=alipay_public_key_string,
    sign_type="RSA2",  # RSA 或者 RSA2
    debug=False,  # 默认 False
    verbose=False,  # 输出调试数据
    # config=AliPayConfig(timeout=15)  # 可选，请求超时时间
)

subject = '测试订单'
alipay_url = 'https://openapi.alipaydev.com/gateway.do?'

order_string = alipay.api_alipay_trade_page_pay(
    out_trade_no='20161112',
    total_amount=1,
    subject=subject,
    return_url='http://localhost:8000',
    notify_url='http://localhost:8000/notify'
)

print(alipay_url+order_string)
