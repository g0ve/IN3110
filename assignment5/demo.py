import os
import sys from os
#Dette er en demo
class MyClass:
    x = 5
    print ('Hello, world!')

    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)

    i = 1
    while i < 6:
        print(i)
        i += 1

    def my_function():
        return True


    try:
        print(x)
    except NameError:
        print("Variable x is not defined")
    except:
        print("Something else went wrong")

    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")

    
    a = """Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua."""
    print(a)

    a = '''Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.'''
    print(a)
