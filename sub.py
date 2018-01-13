import redis
import time
r = redis.StrictRedis(host='localhost', port=32770, db=1)
p = r.pubsub()
p.subscribe('test')

while True:
    message = p.get_message()
    if message:
        print "Subscriber: %s" % message['data']
    
