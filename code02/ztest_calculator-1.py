import unittest

from calculator import factorial, add, substraction, multiply, divide


# test the calculator functionality

class TestCalculator(unittest.TestCase):

    
	def testadd(self):
		self.assertEqual(6, add (2,4))
		self.assertEqual(-3, add (1,-4))
		self.assertEqual(0, add (-2,2))
		self.assertEqual(0, add (-2,2))
		self.assertEqual(10, add (5,5))
		self.assertEqual(4, add(6,-2))
					
	def testfactorial(self): 
		self.assertEqual(120, factorial(5))
		self.assertEqual(1, factorial(1))
		self.assertEqual(2, factorial(2))
		self.assertEqual(24, factorial(4))
		self.assertEqual("inf", factorial(-3))
		
	def substraction(self):
		self.assertEqual(120, substraction(140,20))
		self.assertEqual(55, substraction(88, 33))
		self.assertEqual(-1, substraction(2,3))
		self.assertEqual(0, substraction(-50,50))
		self.assertEqual(-20, substraction(-80,-60))
	
	def multiply(self): 
		self.assertEqual("nan", multiply(2,0))
		self.assertEqual(20, multiply(10,2))
		self.assertEqual("nan", mutiply(0,3))
		self.assertEqual(45, multiply(9,5))
		self.assertEqual(-35, multiply(-7,5))
		
	def divide(self):
	
		self.assertEqual("nan", divide(2,0))
		self.assertEqual("nan", divide(0,3))
		self.assertEqual(3, divide(9,3)) 
		self.assertEqual(-5, divide(-1230, 246))
		self.assertEqual(9, divide(-81, -9))

if __name__ == '__main__':
	unittest.main()