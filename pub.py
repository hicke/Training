import redis
import time

queue = redis.StrictRedis(host='localhost', port=32770, db=1)
channel = queue.pubsub()

for i in range(10):
    queue.publish("test", i)
