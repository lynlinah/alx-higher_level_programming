#!/usr/bin/python3

from calculator_1 import add, subtract, multiply, divide

a = 10
b = 5

sum_result = add(a, b)
diff_result = subtract(a, b)
multi_result = multiply(a, b)
div_result = divide(a, b)

print("{} + {} = {}".format(a, b, sum_result))
print("{} - {} = {}".format(a, b, diff_result))
print("{} * {} = {}".format(a, b, multi_result))
print("{} / {} = {}".format(a, b, div_result))
