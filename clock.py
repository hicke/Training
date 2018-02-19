#!/bin/env python3
# -*- coding: utf-8 -*-

import time
import datetime
import sys

# TODO: Create number converter method into graphics


for i in range(10):
    timeticker = datetime.datetime.now().strftime("%H:%M:%S")
    sys.stdout.write("\r{0}".format(timeticker))
    sys.stdout.flush()
    time.sleep(1)

numbers = {
    ":": u'''\

  ██

  ██

        ''',
    "1": u'''\
  ██
████
  ██
  ██
██████''',
    "2": u'''\
██████
    ██
██████
██
██████''',
    "3": u'''\
██████
    ██
██████
    ██
██████''',
    "4": u'''\
██  ██
██  ██
██████
    ██
    ██''',
    "5": u'''\
██████
██  
██████
    ██
██████''',
    "6": u'''\
██████
██  
██████
██  ██
██████''',
    "7": u'''\
██████
    ██  
    ██
    ██
    ██''',
    "8": u'''\
██████
██  ██
██████
██  ██
██████''',
    "9": u'''\
██████
██  ██
██████
    ██
    ██''',
    "0": u'''\
██████
██  ██
██  ██
██  ██
██████'''}


for digits in numbers.values():
    print(digits, end="")
