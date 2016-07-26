import sys

sys.path.append('/var/www/homeautomation/web')

import redis


class redisclient:
    __redisconnection = None

    def __init__(self, address, port):
        redisclient.__redisconnection = redis.StrictRedis(host=address, port=port, db=0, decode_responses=True)

    def get(key):
        return redisclient.__redisconnection.get(key)

    def getasstring(key):
        return redisclient.get(key) #.decode('utf-8')

    def getasint(key):
        return int(redisclient.get(key)) #.decode('utf-8'))

    def set(key, value):
        redisclient.__redisconnection.set(key, value)

    def hget(key, field):
        return redisclient.__redisconnection.hget(key, field)

    def hgetall(key):
        return redisclient.__redisconnection.hgetall(key)

    def hgetasstring(key, field):
        return redisclient.hget(key, field)

    def hgetasint(key, field):
        return int(redisclient.hget(key, field)) #.decode('utf-8'))

    def hset(key, field, value):
        redisclient.__redisconnection.hset(key, field, value)

    def lrange(key, start=0, end=65536):
        return redisclient.__redisconnection.lrange(key, start, end)

    def delete(key):
        redisclient.__redisconnection.delete(key)

    def lpush(key, value):
        redisclient.__redisconnection.lpush(key, value)

    def sadd(key, value):
        redisclient.__redisconnection.sadd(key, value)

    def smembers(key):
        return redisclient.__redisconnection.smembers(key)

    def srem(key, value):
        redisclient.__redisconnection.srem(key, value)

