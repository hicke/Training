import redis

# class Fakeredis():
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
# def build_dict(key, value):
#     for keys, values in key, value:
#         d[keys] = value
#         d[:]

r = redis.StrictRedis(host='localhost', port='32768', db='4')

r.set('henric', '42', 10)
# build_dict('name', 'henric')

mydict = {"apples": 42, "oranges": 999}
mydict["bananas"] = 56
print(mydict)


list_of_names = ['henric', 'nisse', 'olle']


def this_and_that():
    for items in list_of_names:
        items.split()
        print(items)
