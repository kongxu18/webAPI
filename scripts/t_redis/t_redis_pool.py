"""
redis 池子 单例模式
"""
import redis
POOL = redis.ConnectionPool(host='175.24.179.83',
                            port=6379,
                            password='333333',
                            max_connections=100,
                            )
