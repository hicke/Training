import redis
import time
r = redis.StrictRedis(host='localhost', port=32768, db=1)
p = r.pubsub()
p.subscribe('parse')

while True:
    message = p.get_message()
    if message:
        print("Subscriber: %s" % message['data'])
