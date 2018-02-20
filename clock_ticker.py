import time
import sys
import datetime

while True:
    timeticker = datetime.datetime.now().strftime('%H:%M:%S')
    sys.stdout.write(timeticker)
    time.sleep(0.5)
    sys.stdout.flush()