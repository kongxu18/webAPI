from rest_framework.throttling import SimpleRateThrottle
from rest_framework.request import Request


class SMSThrottling(SimpleRateThrottle):
    scope = 'sms'
    is_send = True

    def get_cache_key(self, request, view):
        phone = request.query_params.get('telephone')
        # 'throttle_%(scope)s_%(ident)s'
        if not self.is_send:
            return None

        return self.cache_format % {'scope': self.scope, 'ident': phone}
