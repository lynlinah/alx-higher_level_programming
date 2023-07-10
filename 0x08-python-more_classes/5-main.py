#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
<<<<<<< HEAD
        print(my_rectangle)
except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
=======
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
>>>>>>> ac02f08a0357eeb9e9495ed6bd6cab6f0145d8e4
