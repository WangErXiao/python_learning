import redis
pool=redis.ConnectionPool(host='localhost',port=6379,db=0)
r=redis.Redis(connection_pool=pool)
pipe=r.pipeline()
pipe.set('yao','wang')
pipe.get('foo')
print(pipe.execute())

