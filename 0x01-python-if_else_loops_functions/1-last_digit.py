#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
last = abs(number) % 10
last = -last if number < 0 else last

if last > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last))
elif (last < 6) and not(last == 0):
    print("Last digit of {} is {} and is less than "
          "6 and not 0".format(number, last))
else:
    print("Last digit of {} is {} and is 0".format(number, last))
