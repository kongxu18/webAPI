"""
python 控制redis
"""
from redis import Redis

conn = Redis(host='175.24.179.83', port=6379, password='333333')
res = conn.get('name')
print(res)

"""
redis 连接池
"""
import redis
from t_redis_pool import POOL

"""
pool 应该使用单例模式，不然执行一次就会创造一个池子
"""

# 只要执行这句，就会从池子里拿到一个连接
conn = redis.Redis(connection_pool=POOL)
res = conn.get('name')

"""
字符串操作
set 用法
    ex 过期时间 秒
    px 过期时间 毫秒
    nx True 如果key值存在，就不操作。如果不存在就新增，set操作才有效
    xx true 如果key值存在，set才执行，不存在就不会操作

get 用法

"""
conn.set('height', 1810, ex=170, nx=True)
# 批量设置
conn.mset({'a': 1, 'b': 2})

r = conn.mget(['a', 'b'])
print(r)

# 设置新值 并且获取原来的旧值
r1 = conn.getset('a', 123)
print(r1)

# 截取字符串 前闭后闭
r2 = conn.getrange('a', 0, 1)
print(r2)

# 替换字符串 返回一个字符串长度
r3 = conn.setrange('a', 1, 'asdd')
print(r3)

"""
可以统计 页面，接口，文章的访问量
"""
# incr  执行一下，这个数字加一
conn.incr('b')
conn.incr('b')
conn.incr('b')

"""
decr 秒杀场景
"""
# 执行一次减一
conn.decr('b')

# 追加字符串
conn.append('a', 'asdsadasd')

"""
hash 操作

"""
conn.hset('hash1', 'a', '123')
conn.hset('hash1', 'b', '123')

ret = conn.hget('hash1', 'a')
print(ret)

conn.hset('hash2', mapping={'a': '1', 'b': '2'})

ret = conn.hmget('hash1', 'a', 'b')
ret = conn.hmget('hash1', ['a', 'b'])
print(ret)

# 获取name 对应 hash中键的个数
conn.hlen('hash1')

# 获取所有keys
conn.hkeys('hash1')

# 获取所有values
conn.hvals('hash1')

# 判断 有没有key
conn.hexists('hash1', 'a')

# 删除
conn.hdel('hash1', 'a', 'b')

# val 增加1
conn.hincrby('hash2', 'a')

# 有点像分页，获取数据，一片一片取
"""
假设一万条数据，先取出100条，把这100条做成生成器
100条用完了再取100条
"""
ret = conn.hscan_iter('hash2')
print(ret)
for i in ret:
    print(i)

"""
列表操作
"""
# 从左边添加
conn.lpush('list1', 1, 23, 4, 5, 6)
# 从右边添加
conn.rpush('list2', 7, 8, 9, 10)

"""
只有存在列表key 列表才会新增
"""
conn.lpushx('list1', 111)

# 统计长度
conn.llen('list1')

# 插入 ,在指定 值得位置前后插入
conn.linsert('list1', 'after', '111', '77777')

# 给某个位置 重新赋值
conn.lset('list1', '3', '2a')

# 指定删除
# count 》 0 从前往后删除几个
# count 《 0 从后往前删除几个
# count = 0 全部删除
conn.lrem('list1', 1, '5')

# 弹出元素
conn.lpop('list1')
conn.rpop('list1')

# 获取对应index 的 值
conn.lindex('list1', 1)

# 切片
conn.lrange('list1', 0, 2)

# 移除不在区间的内容
conn.ltrim('list1', 1, 2)

#
# conn.rpoplpush('list1','list2')

"""
block 阻塞弹出
每次左侧弹出，当无数据可弹出，就阻塞等待

场景：分布式爬虫
消息队列
"""
conn.blpop('list1')
conn.brpop('list1', timeout=10)

"""
自定制 分批取列表数据
每次只取出一部分，用完再取做成生成器
"""
list1 = [i for i in range(100)]
conn.rpush('list3', *list1)

print('---------------------------------')


def scan_list(name, count=2):
    index = 0
    while True:
        # 从 0 开始 取出 2个，对应索引 0，1
        data_list = conn.lrange(name, index, count + index - 1)
        if not data_list:
            return
        index += count
        yield from data_list
        # for i in data_list:
        #     yield i


# for item in scan_list('list3', 5):
#     print('---')
#     print(item)

fun = scan_list('list3', 5)
print(next(fun))

"""
管道 实现事务
默认情况下是原子性操作，要么全部成功，要么都失败
比如转账：a 扣除100，b增加100，如果断电，则都不能实现操作。
不能只执行一部分
"""
conn = redis.Redis(connection_pool=POOL)
# 管道 transaction:事务 true
pipe = conn.pipeline(transaction=True)
pipe.multi()
pipe.set('name','alex')
pipe.set('role','sb')

# 这句话才会正在执行
pipe.execute()


"""
redis 其他操作
"""
# 删除
conn.delete('hash1')

# 判断name在不在
conn.exists('hash1')

# 查询出 正则匹配的个数
conn.keys('name*')

# 设置过期时间
conn.expire('hash2',2)

# 随机抽取
conn.randomkey()

# 查看类型
conn.type('name')