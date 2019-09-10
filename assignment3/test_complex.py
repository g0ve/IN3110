#!/usr/bin/env python

from complex import Complex
import math

"""
Tests if __con__ works has it should
"""
def test_con_two_pos():
    x = Complex(1, 2)
    assert x.conjugate() == Complex(1, -2)

def test_con_one_neg_one_pos():
    x = Complex(5, -6)
    assert x.conjugate() == Complex(5, 6)

def test_con_0_one_neg():
    x = Complex(0, -9)
    assert x.conjugate() == Complex(0, 9)

def test_con_0_one_pos():
    x = Complex(0, 4)
    assert x.conjugate() == Complex(0, -4)

def test_con_one_pos_0():
    x = Complex(10, 0)
    assert x.conjugate() == Complex(10, 0)

"""
Tests if __mod__ works has it should
"""
def test_mod_two_pos():
    x = Complex(1, 7)
    assert x.modulus() == math.sqrt(50)

def test_mod_one_neq_one_pos():
    x = Complex(-3, 4)
    assert x.modulus() == math.sqrt(25)

def test_mod_one_pos_one_neg():
    x = Complex(3, -5)
    assert x.modulus() == math.sqrt(34)

def test_mod_two_neg():
    x = Complex(-6, -4)
    assert x.modulus() == math.sqrt(52)

"""
Tests if __add__ works has it should
"""
def test_add_pos():
    x = Complex(1, 9)
    y = Complex(7, 5)
    assert (x + y) == Complex(8, 14) # 8+14i

def test_add_0():
    x = Complex(0, 0)
    y = Complex(0, 0)
    assert (x + y) == Complex(0, 0) # 0

def test_add_con():
    x = Complex(9, 0)
    y = Complex(20, 0)
    assert (x + y) == Complex(29, 0) # 29

def test_add_i():
    x = Complex(0, 0)
    y = Complex(0, 1)
    assert (x + y) == Complex(0, 1) # i

def test_add_imag():
    x = Complex(0, 13)
    y = Complex(0, 1)
    assert (x + y) == Complex(0, 14) # 14i

def test_add_neg_i():
    x = Complex(0, 0)
    y = Complex(0, -1)
    assert (x + y) == Complex(0, -1) # -i

def test_add_neg_imag():
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

def test_sub_0():
    x = Complex(0, 0)
    y = Complex(0, 0)
    assert (x - y) == Complex(0, 0) # 0

def test_sub_const():
    x = Complex(20, 0)
    y = Complex(9, 0)
    assert (x - y) == Complex(11, 0) # 11

def test_sub_i():
    x = Complex(0, 11)
    y = Complex(0, 10)
    assert (x - y) == Complex(0, 1) # i

def test_sub_imag():
    x = Complex(0, 13)
    y = Complex(0, 1)
    assert (x - y) == Complex(0, 12) # 12i

def test_sub_neg_i():
    x = Complex(0, -1)
    y = Complex(0, 0)
    assert (x - y) == Complex(0, -1) # -i

def test_sub_neg_imag():
    x = Complex(0, -14)
    y = Complex(0, -1)
    assert (x - y) == Complex(0, -13) # -13i

"""
Tests if __mul__ works has it should
"""
def test_mul_all_pos():
    x = Complex(4, 6)
    y = Complex(2, 1)
    assert (x * y) == Complex(2, 16)

def test_mul_one_complex_neg():
    x = Complex(-4, -6)
    y = Complex(2, 1)
    assert (x * y) == Complex(-2, -16)

def test_mul_one_neg():
    x = Complex(2, 1)
    y = Complex(4, -3)
    assert (x * y) == Complex(11, -2)

def test_mul_0():
    x = Complex(0, 0)
    y = Complex(0, 0)
    assert (x * y) == Complex(0, 0)

"""
Tests if __eq__ works has it should
"""
def test_eq_all_pos():
    x = Complex(1, 2)
    assert x == Complex(1, 2)

def test_eq_self_neg():
    x = Complex(-3, 4)
    assert x == Complex(-3, 4)

def test_eq_other_neg():
    x = Complex(5, -6)
    assert x == Complex(5, -6)

def test_eq_all_neg():
    x = Complex(-7, -8)
    assert x == Complex(-7, -8)

def test_eq_self_0():
    x = Complex(0, 9)
    assert x == Complex(0, 9)

def test_eq_other_0():
    x = Complex(10, 0)
    assert x == Complex(10, 0)

def test_eq_0():
    x = Complex(0, 0)
    assert x == Complex(0, 0)
