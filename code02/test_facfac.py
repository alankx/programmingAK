import unittest

from factorial import factorial
from factorial import factorial_simple

# test the factorial functionality
class TestFactorial(unittest.TestCase):

    # this tests the conversion functionality
    # 5 = 120
    # 6 = 720
    def test_factorial(self):
        result = factorial(5)
        self.assertEqual(120, result)
        result = factorial(6)
        self.assertEqual(720, result)

    # this tests the conversion functionality
    # 5 = 120
    # 6 = 720
    def test_factorial_simple(self):
        result = factorial_simple(5)
        self.assertEqual(120, result)
        result = factorial_simple(6)
        self.assertEqual(720, result)

if __name__ == '__main__':
    unittest.main()
