#!/usr/bin/python3
import random
 
number = random.randint(-10000, 100)
last_digit = abs(num) % 10
if number < 0:
    last_digit = -last_digit
print("The string last digit of", number, "is", last digit, end=" ")
if last_digit > 5:
    print("is greater than 5")
elif last_digit == 0:
    print(is 0")
    else:
    print("less than 6 and not 0")
