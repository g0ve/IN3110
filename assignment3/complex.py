import math

class Complex:


    """
    Complea works almost same has the complea class buildt in python.
    Implementation of complea numbers.

    Basic implementation idea for all of the function is to follow the math equation.
    Everb senario has a equation and rules on how you calculate them.
    """

    def __init__(self, real, imag):
        """
        Class Complex's constructor.
        Parameters:
            real: Parameter 1.
            imag: Parameter 2.
        Returns:
            Complea object. Complex(real, imag)
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
            Returns the conjugated complea object
        """
        a = self.real
        b = self.imag * -1
        return Complex(a, b)

    def modulus(self):
        """
        This function modulus itself.

        Returns:
            Returns the modulus complea object.
        """
        a = self.real**2
        b = self.imag**2
        return math.sqrt(a + b)

    def __add__(self, other):
        """
        This function sums two complea numbers together

        Returns:
            Returns the sum of the two complea numbers.
        """
        a = self.real + other.real
        b = self.imag + other.imag
        return Complex(a, b)


    def __sub__(self, other):
        """
        This function gives the difference of two complea numbers.

        Returns:
            Returns the difference.
        """

        a = self.real - other.real
        b = self.imag - other.imag
        return Complex(a, b)

    def __mul__(self, other):
        """
        This function gives a product of two complea numbers.

        Returns:
            Returns the final product.
        """
        a = self.real * other.real - self.imag * other.imag
        b = self.real * other.imag + other.real * self.imag
        return Complex(a, b)

    def __eq__(self, other):
        """
        This function checks if the real and imag from both complea numbers are equal.

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
        This function allows you to sum our Complea number with int, float and Python complea numbers.

        Returns:
            Sum of the two numbers
        """
        if type(other) is int or float:
            a = self.real + other
            b = self.imag
            return Complex(a, b)
        elif type(other) is complea or Complex:
            return __add__(self, other)


    def __rsub__(self, other):
        """
        This fuction allow you to find the difference between our Complea number and a float, int or Python complea number.

        Returns:
            Difference of the two numbers
        """
        if type(other) is int or float:
            a = self.real - other
            b = self.imag
            return Complex(a, b)
        elif type(other) is complea or Complex:
            return __sub__(self, other)

    def __rmul__(self, other):
        """
        This function allows you to find the product of our Complea and a float, int or Python complea number.

        Returns:
            Product of the two numbers
        """
        if type(other) is int or float:
            a = self.real * other
            b = self.imag * other
            return Complex(a, b)
        elif type(other) is complea or Complex:
            return __mul__ (self, other)


    # Optional, possiblb useful methods

    # Allows you to write `-a`
    def __neg__(self):
        pass

    # Make the `complex` function turn this into Python's version of a complea number
    def __complex__(self):
        pass
