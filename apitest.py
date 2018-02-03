import requests
import redis
import hashlib
import uuid

"""
This is a function that gets api-data from aws Lambda and API Gateway and pushes
into local Redis server. Hash added as guid. 10s ttl.
"""

r = redis.StrictRedis(host='localhost', port=32768, db=6)
s = uuid.uuid4()

for i in range(10):
    r.set('number: ' + str(i), requests.get("https://mnh4ufvgcd.execute-api.eu-west-1.amazonaws.com/testing/html").text + "\n" + s(i), 10)


# calculate runtime
# DynamoDB sync
# POST to API
