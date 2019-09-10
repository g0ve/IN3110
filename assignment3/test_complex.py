#!/usr/bin/env python

from complex import Complex
import math

"""
Tests if __con__ works has it should
"""
def test_con():

    x = Complex(1, 2)
    #1 - 2i
    assert x.conjugate() == Complex(1, -2)

    x = Complex(5, -6)
    #5 + 6i
    assert x.conjugate() == Complex(5, 6)

    x = Complex(0, -9)
    #9i
    assert x.conjugate() == Complex(0, 9)

    x = Complex(0, 4)
    #-4i
    assert x.conjugate() == Complex(0, -4)

    x = Complex(10, 0)
    #10
    assert x.conjugate() == Complex(10, 0)

"""
Tests if __mod__ works has it should
"""
def test_mod():
    x = Complex(1, 7)
    #7.0710
    assert x.modulus() == math.sqrt(50)

    x = Complex(-3, 4)
    #5
    assert x.modulus() == math.sqrt(25)

    x = Complex(3, -5)
    #5.8309
    assert x.modulus() == math.sqrt(34)

    x = Complex(-6, -4)
    #7.2111
    assert x.modulus() == math.sqrt(52)

"""
Tests if __add__ works has it should
"""
def test_add():
    x = Complex(1, 9)
    y = Complex(7, 5)
    assert (x + y) == Complex(8, 14) # 8+14i

    x = Complex(0, 0)
    y = Complex(0, 0)
    assert (x + y) == Complex(0, 0) # 0

    x = Complex(9, 0)
    y = Complex(20, 0)
    assert (x + y) == Complex(29, 0) # 29

    x = Complex(0, 0)
    y = Complex(0, 1)
    assert (x + y) == Complex(0, 1) # i

    x = Complex(0, 13)
    y = Complex(0, 1)
    assert (x + y) == Complex(0, 14) # 14i

    x = Complex(0, 0)
    y = Complex(0, -1)
    assert (x + y) == Complex(0, -1) # -i

    x = Complex(0, -14)
    y = Complex(0, -1)
    assert (x + y) == Complex(0, -15) # -15i

"""
Tests if __sub__ works has it should
"""
def test_sub():
    x = Complex(1, 9)
    y = Complex(7, 5)
    assert (x - y) == Complex(-6, 4) # 8-14i

    x = Complex(0, 0)
    y = Complex(0, 0)
    assert (x - y) == Complex(0, 0) # 0

    x = Complex(20, 0)
    y = Complex(9, 0)
    assert (x - y) == Complex(11, 0) # 11

    x = Complex(0, 11)
    y = Complex(0, 10)
    assert (x - y) == Complex(0, 1) # i

    x = Complex(0, 13)
    y = Complex(0, 1)
    assert (x - y) == Complex(0, 12) # 12i

    x = Complex(0, -1)
    y = Complex(0, 0)
    assert (x - y) == Complex(0, -1) # -i

    x = Complex(0, -14)
    y = Complex(0, -1)
    assert (x - y) == Complex(0, -13) # -13i

"""
Tests if __mul__ works has it should
"""
def test_mul():
    #x = self.real * other.real - self.imaginary * other.imaginary
    #y = self.real * other.imaginary + self.imaginary * other.real

    x = Complex(4, 6)
    y = Complex(2, 1)
    #32i
    assert (x * y) == Complex(2, 16)

    x = Complex(-4, -6)
    y = Complex(2, 1)
    #-2-16i
    assert (x * y) == Complex(-2, -16)

    x = Complex(2, 1)
    y = Complex(4, -3)
    #12-2i
    assert (x * y) == Complex(11, -2)

    x = Complex(0, 0)
    y = Complex(0, 0)
    #0
    assert (x * y) == Complex(0, 0)

"""
Tests if __eq__ works has it should
"""
def test_eq():
    x = Complex(1, 2)
    assert x == Complex(1, 2)

    x = Complex(-3, 4)
    assert x == Complex(-3, 4)

    x = Complex(5, -6)
    assert x == Complex(5, -6)

    x = Complex(-7, -8)
    assert x == Complex(-7, -8)

    x = Complex(0, 9)
    assert x == Complex(0, 9)

    x = Complex(10, 0)
    assert x == Complex(10, 0)

    x = Complex(0, 0)
    assert x == Complex(0, 0)
