#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNumber = int(str(number)[-1])
if number < 0:
    lastNumber = -lastNumber
if lastNumber > 5:
    print(f"Last digit of {number:d} is {lastNumber:d} and is greater than 5")
elif lastNumber == 0:
    print(f"Last digit of {number:d} is {lastNumber:d} and is 0")
elif lastNumber > 0 and lastNumber < 6:
    print(f"Last digit of {number:d} is {lastNumber:d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {lastNumber:d} and is less than 6 and not 0")
