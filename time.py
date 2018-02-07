import time
import threading
import math
import time
import timeit
from queue import Queue

l = [3,4,5,6]

def cube():
    for i in l:
        print("Cube: " + str(i*i*i))


def square():
    for i in l:
        print("Cube: " + str(i*i))
        


start = time.time()

# t1 = threading.Thread(target=cube)
# t2 = threading.Thread(target=square)

# t1.start()
# t2.start()
# t1.join()
# t2.join()

cube()
square()
done = time.time()
print('Elapsed time for execution:', done-start)


class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())