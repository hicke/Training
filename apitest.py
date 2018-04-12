import requests
import redis
import uuid
import json
# import timeit

"""
This is a function that gets api-data from aws Lambda and API Gateway and pushes
into local Redis server. Hash added as guid. 10s ttl.
"""

r = redis.StrictRedis(host='localhost', port=32768, db=6)

<<<<<<< HEAD
for i in range(10):
    r.set('number: ' + str(i), requests.get("https://mnh4ufvgcd.execute-api.eu-west-1.amazonaws.com/testing/html").text + "\n" + s, 10)
=======
d = {}
d.update({})
for i in range(5):
    h = uuid.uuid4().hex
    # hex = h.hexdigest()
    #r.set('number: ' + str(i), requests.get("https://mnh4ufvgcd.execute-api.eu-west-1.amazonaws.com/testing/html").text + "\n" + h.hexdigest())
    d.update({"hash: " + str(i): h})
    j = json.dumps(d)
r.set("payload", j)
>>>>>>> 56244c842fec5471c0ef59307e10e6ffe1fda407

#
# r = {'is_claimed': 'True', 'rating': 3.5}
# r = json.dumps(r)
# loaded_r = json.loads(r)
# loaded_r['rating'] #Output 3.5
# type(r) #Output str
# type(loaded_r) #Output dict
