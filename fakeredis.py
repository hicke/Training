import redis

# class Fakeredis():
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
    
# def build_dict(key, value):
   
#     for keys, values in key, value:
#         d[keys] = value
#         d[:]

# build_dict('name', 'henric')

# region henric
mydict = {"apples": 42, "oranges": 999}
mydict["bananas"] = 56
print(mydict)
# endregion

list_of_names = ['henric', 'nisse', 'olle']


def this_and_that():
    for items in list_of_names:
        items.split()
        print(items)

this_and_that()
