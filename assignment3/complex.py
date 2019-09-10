#!/usr/bin/env python

import math

class Complex:


    """Complex works almost same has the complex class buildt in python"""

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # Assignment 3.3

    def conjugate(self):
        x = self.real
        y = self.imaginary * -1
        return Complex(x, y)

    def modulus(self):
        x = self.real**2
        y = self.imaginary**2
        return math.sqrt(x + y)

    def __add__(self, other):
        x = self.real + other.real
        y = self.imaginary + other.imaginary
        return Complex(x, y)

    def __sub__(self, other):
        x=self.real - other.real
        y=self.imaginary - other.imaginary
        return Complex(x, y)

    def __mul__(self, other):
        x = self.real * other.real - self.imaginary * other.imaginary
        y = self.real * other.imaginary + self.imaginary * other.real
        return Complex(x, y)

    def __eq__(self, other):
        realBoolean = self.real == other.real
        imaginaryBoolean = self.imaginary == other.imaginary

        return realBoolean and imaginaryBoolean

    # Assignment 3.4
    def __radd__(self, other):
        return __add__(self, other)

    def __rsub__(self, other):
        return __sub__(self, other)

    def __rmul__(self, other):
        return __mul__(self, other)


    # Optional, possibly useful methods

    # Allows you to write `-a`
    def __neg__(self):
        x = self.real * -1
        y = self.imaginary * -1
        return Complex(x, y)

    # Make the `complex` function turn this into Python's version of a complex number
    def __complex__(self):
        x = self.real
        y = self.imaginary * 1j
