# coding=utf-8
import redis
import config

pool = redis.ConnectionPool(host=config.redis_host, port=config.redis_port)
rpool = redis.Redis(connection_pool=pool)