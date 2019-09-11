import math

class Complex:


    """
    Complex works almost same has the complex class buildt in python.
    Implementation of complex numbers.

    Basic implementation idea for all of the function is to follow the math equation.
    Every senario has a equation and rules on how you calculate them.
    """

    def __init__(self, real, imag):
        """
        Class Complex's constructor.
        Parameters:
            real: Parameter 1.
            imag: Parameter 2.
        Returns:
            Complex object. Complex(real, imag)
        """
        self.real = real
        self.imag = imag

    # Assignment 3.3

    def conjugate(self):
        """
        This function conjugate itself.
        Parameters:
            x: first number = real
            y: second number = imag
        Returns:
            Returns the conjugated complex object
        """
        x = self.real
        y = self.imag * -1
        return Complex(x, y)

    def modulus(self):
        """
        This function modulus itself.

        Returns:
            Returns the modulus complex object.
        """
        x = self.real**2
        y = self.imag**2
        return math.sqrt(x + y)

    def __add__(self, other):
        """
        This function sums two complex numbers together

        Returns:
            Returns the sum of the two complex numbers.
        """
        x = self.real + other.real
        y = self.imag + other.imag
        return Complex(x, y)


    def __sub__(self, other):
        """
        This function gives the difference of two complex numbers.

        Returns:
            Returns the difference.
        """
        Parameter
        x=self.real - other.real
        y=self.imag - other.imag
        return Complex(x, y)

    def __mul__(self, other):
        """
        This function gives a product of two complex numbers.

        Returns:
            Returns the final product.
        """
        x = self.real * other.real - self.imag * other.imag
        y = self.real * other.imag + other.real * self.imag
        return Complex(x, y)

    def __eq__(self, other):
        """
        This function checks if the real and imag from both complex numbers are equal.

        Returns:
        If both real numbers are equal it returns True AND
        If both imag numbers are equal it returs True ==
        True
        """
        realBoolean = self.real == other.real
        imagBoolean = self.imag == other.imag

        return realBoolean and imagBoolean

    # Assignment 3.4
    def __radd__(self, other):
        """
        This function allows you to sum our Complex number with int, float and Python complex numbers.

        Returns:
            Sum of the two numbers
        """
        if type(other) is int or float:
            x = self.real + other
            y = self.imag
            return Complex(x, y)
        elif type(other) is complex or Complex:
            return __add__(self, other)


    def __rsub__(self, other):
        """
        This fuction allow you to find the difference between our Complex number and a float, int or Python complex number.

        Returns:
            Difference of the two numbers
        """
        if type(other) is int or float:
            x = self.real - other
            y = self.imag
            return Complex(x, y)
        elif type(other) is complex or Complex:
            return __sub__(self, other)

    def __rmul__(self, other):
        """
        This function allows you to find the product of our Complex and a float, int or Python complex number.

        Returns:
            Product of the two numbers
        """
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
