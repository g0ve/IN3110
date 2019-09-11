#!/usr/bin/env python

import math
import cmath

class Complex:


    """Complex works almost same has the complex class buildt in python"""

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Assignment 3.3

    def conjugate(self):
        x = self.real
        y = self.imag * -1
        return Complex(x, y)

    def modulus(self):
        x = self.real**2
        y = self.imag**2
        return math.sqrt(x + y)

    def __add__(self, other):
        x = self.real + other.real
        y = self.imag + other.imag
        return Complex(x, y)


    def __sub__(self, other):
        x=self.real - other.real
        y=self.imag - other.imag
        return Complex(x, y)

    def __mul__(self, other):
        x = self.real * other.real - self.imag * other.imag
        y = self.real * other.imag + other.real * self.imag
        return Complex(x, y)

    def __eq__(self, other):
        realBoolean = self.real == other.real
        imagBoolean = self.imag == other.imag

        return realBoolean and imagBoolean

    # Assignment 3.4
    """
    Here I have added to codes that should work. When i run it on my computer it doesnt work.
    But if someone else copy my code and run it. It works..
    """
    def __radd__(self, other):
        if type(other) is int or float:
            x = self.real + other
            y = self.imag
            return Complex(x, y)
        elif type(other) is complex or Complex:
            return __add__(self, other)


    def __rsub__(self, other):
        if type(other) is int or float:
            x = self.real - other
            y = self.imag
            return Complex(x, y)
        elif type(other) is complex or Complex:
            return __sub__(self, other)

    def __rmul__(self, other):
        if type(other) is int or float:
            x = self.real * other
            y = self.imag * other
            return Complex(x, y)
        elif type(other) is complex or Complex:
            return __mul__ (self, other)


    # Optional, possibly useful methods

    # Allows you to write `-a`
    def __neg__(self):
        pass

    # Make the `complex` function turn this into Python's version of a complex number
    def __complex__(self):
        pass
