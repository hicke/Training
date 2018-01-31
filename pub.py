import redis
import time

<<<<<<< HEAD
queue = redis.StrictRedis(host='localhost', port=32770, db=4)
r = redis.StrictRedis(host='localhost', port=32770, db=4)
channel = queue.pubsub()

for i in range(10):
    queue.publish("test", "This is message %s" % str(i))
    r.set('Number', i, 15)
=======

queue = redis.StrictRedis(host='localhost', port=32768, db=1)
channel = queue.pubsub()

for i in range(100):
    queue.publish("parse", "This is a message: " + str(i) + ' homo')
>>>>>>> 742dccf022f065f21438a9f52e734218e6cb0c40
