#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0:
            print("Fizz", end="")
        elif n % 5 == 0:
            print("Buzz", end="")
        else:
            print(n, end="")
        print(' ', end="")
