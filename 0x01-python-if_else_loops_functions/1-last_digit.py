#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = int(str(number)[-1])
cond = "greater than 5" if n > 5 else \
       "less than 6 and not 0" if n > 0 else \
       "zero"
print("Last digit of {:d} is {:d} and is {}".format(number, n, cond))
