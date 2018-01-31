import redis
import time

queue = redis.StrictRedis(host='localhost', port=32770, db=4)
r = redis.StrictRedis(host='localhost', port=32770, db=4)
channel = queue.pubsub()

for i in range(10):
    queue.publish("test", "This is message %s" % str(i))
    r.set('Number', i, 15)
