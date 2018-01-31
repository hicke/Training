import redis
import time
<<<<<<< HEAD
r = redis.StrictRedis(host='localhost', port=32770, db=4)
=======
r = redis.StrictRedis(host='localhost', port=32768, db=1)
>>>>>>> 742dccf022f065f21438a9f52e734218e6cb0c40
p = r.pubsub()
p.subscribe('parse')

while True:
    message = p.get_message()
    if message:
<<<<<<< HEAD
        print "Subscriber: %s" % message['data']
=======
        print("Subscriber: %s" % message['data'])
>>>>>>> 742dccf022f065f21438a9f52e734218e6cb0c40
