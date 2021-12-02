from day_1 import count_increases
import unittest

class TestSum(unittest.TestCase):

	def test_empty(self):
		self.assertEqual(count_increases([]), 0, "Should be 0 for empty list")

	def test_no_increases(self):
		self.assertEqual(count_increases([5,5,5,5,4,3,2,1]), 0, "Should be 0 for no increases")
	
	def test_increases(self):
		self.assertEqual(count_increases([199,200,208,210,200,207,240,269,260,263]), 7, "Should count increases")

if __name__ == '__main__':
	unittest.main()
