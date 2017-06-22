#student number: 10366826
#student name: alan kirwan

import unittest

class Calculator():

    # defining calculator operations with input validations
    def add(self,x,y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x+y
        else:
            raise ValueError

    def subtract(self,x,y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x-y
        else:
            raise ValueError

    def multiply(self,x,y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x*y
        else:
            raise ValueError

    def divide(self,x,y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            if y == 0:
                return 'NaN'
            return x/y
        else:
            raise ValueError

    def exponent(self,x,y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x**y
        else:
            raise ValueError

    def square(self,x):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types):
            return x*x
        else:
            raise ValueError

    def squareroot(self,x):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types):
            return x**0.5
        else:
            raise ValueError

    def cube(self,x):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types):
            return x**3.0
        else:
            raise ValueError

    def sine(self,x,y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x/y
        else:
            raise ValueError

    def cosine(self,x,y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x/y
        else:
            raise ValueError


# Testing the calculator functionality

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

	# this tests the add functionality
	# 2 + 2 = 4
	# 2 + 4 = 6
	# 2 + (-2) = 0
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
        result = self.calc.add(2,4)
        self.assertEqual(6, result)
        result = self.calc.add(2, -2)
        self.assertEqual(0, result)

    # Testing subtract functionality
    # 2 - 2 = 0
    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract(2, 2)
        self.assertEqual(0, result)
        result = self.calc.subtract(2,4)
        self.assertEqual(-2, result)
        result = self.calc.subtract(2, -4)
        self.assertEqual(6, result)

    # Testing for valid numberical input
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
        self.assertRaises(ValueError, self.calc.subtract, 'two', 'three')

    # Testing multiplication functionality
    # 2 x 2 = 4
    # 2 x 4 = 8
    def test_calculator_multiply_method_returns_correct_result_for_2_params_the_same(self):
        result = self.calc.multiply(2, 2)
        self.assertEqual(4, result)
        result = self.calc.multiply(2, 4)
        self.assertEqual(8, result)
        result = self.calc.multiply(2, -2)
        self.assertEqual(-4, result)
        result = self.calc.multiply(2, 0)
        self.assertEqual(0, result)
        result = self.calc.multiply(2, 0)
        self.assertEqual(0, result)

    # Testing divide functionality
    # 2 / 2 = 1
    # 4 / 2 = 2
    def test_calculator_divide_method_returns_correct_result_for_2_params_the_same(self):
        result = self.calc.divide(2, 2)
        self.assertEqual(1, result)
        result = self.calc.divide(4, 2)
        self.assertEqual(2, result)
        result = self.calc.divide(2, -2)
        self.assertEqual(-1, result)
        result = self.calc.divide(-100, -10)
        self.assertEqual(10, result)
        result = self.calc.divide(2, 0)
        self.assertEqual('NaN', result)
        self.assertRaises(ValueError, self.calc.divide, 'two', 'three')
        self.assertRaises(ValueError, self.calc.divide, 'two', 0)
        self.assertRaises(ValueError, self.calc.divide, 2, 'three')

    # Testing exponent functionality
    # 2 to power of 2 = 4
    # 2 to power of 4 = 16
    def test_calculator_exponent_method_returns_correct_result_for_2_params_the_same(self):
        result = self.calc.exponent(2, 2)
        self.assertEqual(4, result)
        result = self.calc.exponent(2, 4)
        self.assertEqual(16, result)
        result = self.calc.exponent(2, -2)
        self.assertEqual(0.25, result)
        result = self.calc.exponent(2, 0)
        self.assertEqual(1, result)

    # Testing square functionality
    # 2 squared = 4
    # 3 squared = 9
    def test_calculator_square_method_returns_correct_result_for_2_params_the_same(self):
        result = self.calc.square(2)
        self.assertEqual(4, result)
        result = self.calc.square(3)
        self.assertEqual(9, result)
        result = self.calc.square(5)
        self.assertEqual(25, result)
        result = self.calc.square(-10)
        self.assertEqual(100, result)

    # Testing squareroot functionality
    # Squareroot of 4 = 2
    # Squareroot of 9 = 3
    def test_calculator_squareroot_method_returns_correct_result_for_2_params_the_same(self):
        result = self.calc.squareroot(4)
        self.assertEqual(2, result)
        result = self.calc.squareroot(9)
        self.assertEqual(3, result)
        result = self.calc.squareroot(25)
        self.assertEqual(5, result)
        result = self.calc.squareroot(100)
        self.assertEqual(10, result)

    # Testing cube functionality
    # 1 cubed = 1
    # 4 cubed = 64
    def test_calculator_cube_method_returns_correct_result_for_2_params_the_same(self):
        result = self.calc.cube(1)
        self.assertEqual(1, result)
        result = self.calc.cube(4)
        self.assertEqual(64, result)
        result = self.calc.cube(5)
        self.assertEqual(125, result)
        result = self.calc.cube(7)
        self.assertEqual(343, result)

    # Testing sine functionality
    # Sin value of 2.8 opposite and 4.9 hypotenuse = 0.5714285714285714
    # Sin value of 0.454 opposite and 0.822 hypotenuse = 0.5523114355231145
    def test_calculator_sine_method_returns_correct_result_for_2_params_the_same(self):
        result = self.calc.sine(2.8, 4.9)
        self.assertEqual(0.5714285714285714, result)
        result = self.calc.sine(0.454, 0.822)
        self.assertEqual(0.5523114355231145, result)
        result = self.calc.sine(3.8, 5.9)
        self.assertEqual(0.6440677966101694, result)
        result = self.calc.sine(-0.515, -1.5)
        self.assertEqual(0.3433333333333333, result)

    # Testing cosine functionality
    # Cos value of 4.0 adjacent and 4.9 hypotenuse = 0.8163265306122448
    # Cos value of 0.454 adjacent and 0.560 hypotenuse = 0.8107142857142856
    def test_calculator_cosine_method_returns_correct_result_for_2_params_the_same(self):
        result = self.calc.cosine(4.0, 4.9)
        self.assertEqual(0.8163265306122448, result)
        result = self.calc.cosine(0.454, 0.560)
        self.assertEqual(0.8107142857142856, result)
        result = self.calc.cosine(8.0, 10.2)
        self.assertEqual(0.7843137254901962, result)
        result = self.calc.cosine(-0.883, -1.5)
        self.assertEqual(0.5886666666666667, result)

if __name__ == '__main__':
    unittest.main()
