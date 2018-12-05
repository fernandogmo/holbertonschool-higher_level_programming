#!/usr/bin/python3
import random
n = random.randint(-10, 10)
sign = "positive" if n > 0 else "negative" if n < 0 else "zero"
print("{:d} is {}".format(n, sign))
