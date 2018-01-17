import redis
import time

queue = redis.StrictRedis(host='localhost', port=32768, db=1)
channel = queue.pubsub()

for i in range(1):
    queue.publish("testchannel", "This is a message: " + str(i))
