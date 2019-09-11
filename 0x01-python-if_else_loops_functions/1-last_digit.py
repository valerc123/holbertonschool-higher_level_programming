#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number >= 0):
    ldigit = number % 10
else:
    ldigit = (abs(number) % 10) * -1
if (ldigit > 5):
    end = "and is greater than 5"
elif (ldigit == 0):
    end = "and is 0"
else:
    end = "and is less than 6 and not 0"
print("Last digit of {:d} is {:d}".format(number, ldigit), end)
