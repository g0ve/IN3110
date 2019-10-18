import os
import sys
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
