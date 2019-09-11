import math
from complex import Complex

"""
For this test file. I choose to make a function for everb test. (Got this tip from a group teacher)
Im not adding a comment to all of the function, but i added a comment for each type of test.
And seperate them after what function in complea theb tests.

Short version: each test part test a function in complex,
and each part has function testing with diffrent kind of numbers.
"""


"""
Tests if __con__ works as it should
"""
def test_con_two_pos():
    a = Complex(1, 2)
    assert a.conjugate() == Complex(1, -2)

def test_con_one_neg_one_pos():
    a = Complex(5, -6)
    assert a.conjugate() == Complex(5, 6)

def test_con_0_one_neg():
    a = Complex(0, -9)
    assert a.conjugate() == Complex(0, 9)

def test_con_0_one_pos():
    a = Complex(0, 4)
    assert a.conjugate() == Complex(0, -4)


"""
Tests if __mod__ works as it should
"""
def test_mod_two_pos():
    a = Complex(1, 7)
    assert a.modulus() == math.sqrt(50)

def test_mod_one_neq_one_pos():
    a = Complex(-3, 4)
    assert a.modulus() == math.sqrt(25)

def test_mod_one_pos_one_neg():
    a = Complex(3, -5)
    assert a.modulus() == math.sqrt(34)

def test_mod_two_neg():
    a = Complex(-6, -4)
    assert a.modulus() == math.sqrt(52)

"""
Tests if __add__ works as it should
"""
def test_add_pos():
    a = Complex(1, 9)
    b = Complex(7, 5)
    assert (a + b) == Complex(8, 14)

def test_add_0():
    a = Complex(0, 0)
    b = Complex(0, 0)
    assert (a + b) == Complex(0, 0)

def test_add_con():
    a = Complex(9, 0)
    b = Complex(20, 0)
    assert (a + b) == Complex(29, 0)

def test_add_i():
    a = Complex(0, 0)
    b = Complex(0, 1)
    assert (a + b) == Complex(0, 1)

def test_add_imag():
    a = Complex(0, 13)
    b = Complex(0, 1)
    assert (a + b) == Complex(0, 14)

def test_add_neg_i():
    a = Complex(0, 0)
    b = Complex(0, -1)
    assert (a + b) == Complex(0, -1)

def test_add_neg_imag():
    a = Complex(0, -14)
    b = Complex(0, -1)
    assert (a + b) == Complex(0, -15)

"""
Tests if __sub__ works as it should
"""
def test_sub():
    a = Complex(1, 9)
    b = Complex(7, 5)
    assert (a - b) == Complex(-6, 4)

def test_sub_0():
    a = Complex(0, 0)
    b = Complex(0, 0)
    assert (a - b) == Complex(0, 0)

def test_sub_const():
    a = Complex(20, 0)
    b = Complex(9, 0)
    assert (a - b) == Complex(11, 0)

def test_sub_i():
    a = Complex(0, 11)
    b = Complex(0, 10)
    assert (a - b) == Complex(0, 1)

def test_sub_imag():
    a = Complex(0, 13)
    b = Complex(0, 1)
    assert (a - b) == Complex(0, 12)

def test_sub_neg_i():
    a = Complex(0, -1)
    b = Complex(0, 0)
    assert (a - b) == Complex(0, -1)

def test_sub_neg_imag():
    a = Complex(0, -14)
    b = Complex(0, -1)
    assert (a - b) == Complex(0, -13)

"""
Tests if __mul__ works as it should
"""
def test_mul_all_pos():
    a = Complex(4, 6)
    b = Complex(2, 1)
    assert (a * b) == Complex(2, 16)

def test_mul_one_complex_neg():
    a = Complex(-4, -6)
    b = Complex(2, 1)
    assert (a * b) == Complex(-2, -16)

def test_mul_one_neg():
    a = Complex(2, 1)
    b = Complex(4, -3)
    assert (a * b) == Complex(11, -2)

def test_mul_0():
    a = Complex(0, 0)
    b = Complex(0, 0)
    assert (a * b) == Complex(0, 0)

"""
Tests if __eq__ works as it should
"""
def test_eq_all_pos():
    a = Complex(1, 2)
    assert a == Complex(1, 2)

def test_eq_self_neg():
    a = Complex(-3, 4)
    assert a == Complex(-3, 4)

def test_eq_other_neg():
    a = Complex(5, -6)
    assert a == Complex(5, -6)

def test_eq_all_neg():
    a = Complex(-7, -8)
    assert a == Complex(-7, -8)

def test_eq_self_0():
    a = Complex(0, 9)
    assert a == Complex(0, 9)

def test_eq_other_0():
    a = Complex(10, 0)
    assert a == Complex(10, 0)

def test_eq_0():
    a = Complex(0, 0)
    assert a == Complex(0, 0)

"""
Tests if __radd__ works as it should
"""
def test_radd_int():
    a = Complex(2, 4)
    b = 3
    assert a + b == Complex(5, 4)

def test_radd_float():
    a = Complex(2, 3)
    b = 2.3
    assert a + b == Complex(4.3, 3)

def test_radd_complP():
    a = Complex(2, 3)
    b = complex(2, 2)
    assert a + b == Complex(4, 5)

def test_radd_Compl():
    a = Complex(2, 3)
    b = Complex(2, 4)
    assert a + b == Complex(4, 7)

"""
Tests if __rsub__ works as it should
"""
def test_rsub_int():
    a = Complex(3, 4)
    b = 2
    assert a - b == Complex(1, 4)

def test_rsub_mul_int():
    a = 1 * Complex(3, 4)
    b = 2
    assert a - b == Complex(1, 4)

def test_rsub_float():
    a = Complex(4, 3)
    b = 2.5
    assert a - b == Complex(1.5, 3)

def test_rsub_complP():
    a = Complex(4, 3)
    b = complex(2, 2)
    assert a - b == Complex(2, 1)

def test_rsub_Compl():
    a = Complex(2, 4)
    b = Complex(2, 3)
    assert a - b == Complex(0, 1)

"""
Tests if __rmul__ works as it should
"""
def test_rmul_int():
    a = Complex(3, 4)
    b = 2
    assert a * b == Complex(6, 8)

def test_rmul_float():
    a = Complex(4, 3)
    b = 2.5
    assert a * b == Complex(10, 7.5)

def test_rmul_complP():
    a = Complex(4, 6)
    b = complex(2, 1)
    assert a * b == Complex(2, 16)

def test_rmul_Compl():
    a = 2 * Complex(2, 3)
    b = complex(2, 1)
    assert a * b == Complex(2, 16)
