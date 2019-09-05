#!/usr/bin/env python

"""
Tests if __add__ works has it should
"""
def add_test():
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
def sub_test():
    x = Complex(1, 9)
    y = Complex(7, 5)
    assert (x - y) == Complex(8, 14) # 8-14i

    x = Complex(0, 0)
    y = Complex(0, 0)
    assert (x - y) == Complex(0, 0) # 0

    x = Complex(9, 0)
    y = Complex(20, 0)
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
Tests if __con__ works has it should
"""
def con_test():

    x = Complex(1, 2)
    assert x.__con__() == Complex(1, 2) # 1 - 2i

    x = Complex(-3, 4)
    assert x.__con__() == Complex(-3, 4) # -3 + 4i

    x = Complex(5, -6)
    assert x.__con__() == Complex(5, -6) # 5 + 6i

    x = Complex(-7, -8)
    assert x.__con__() == Complex(-7, -8) # -7 - 8i

    x = Complex(0, 9)
    assert x.__con__() == Complex(0, 9) # 9i

    x = Complex(10, 0)
    assert x.__con__() == Complex(10, 0) # 10

    x = Complex(0, 0)
    assert x.__con__() == Complex(0, 0) # 0

"""
Tests if __mod__ works has it should
"""
def mod_test():
    x = Complex(-3, 4)
    assert x.__mod__() == math.sqrt(25)

    x = Complex(0, 0)
    assert x.__mod__() == 0

"""
Tests if __eq__ works has it should
"""
def eq_test():
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
