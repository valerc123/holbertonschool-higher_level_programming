#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit=number%10
start = "Last digit of {:d} is {:d}"
if number >= 0 :
        if ldigit > 5 :
                end = "and is greater than 5"
        elif ldigit == 0 :
                end = "and is 0"
        elif ldigit < 6 :
                end = "and is less than 6 and not 0"
print(start.format(number, ldigit) + " " + end)
