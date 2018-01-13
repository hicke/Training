import redis
import boto3
import hashlib
import os
import base64
from pymongo import MongoClient



connection = MongoClient("localhost:32769")

id = base64.urlsafe_b64encode(os.urandom(9)).decode('utf-8')
ids = id[:-3]
re = redis.Redis(host='localhost', port=32770, db=0)
re.set('name' + '_' + ids, id)
print(re.get('name'))
print(id)
print(ids)

# id = base64.urlsafe_b64encode(os.urandom(9)).decode('utf-8')


#
# r = redis.StrictRedis(host='', port=6379, db=0)
# r.set('mullvad', '3844909252002295')
# out = r.get('mullvad')
# print out
