#!/usr/bin/python3

from day3 import *
import unittest

class Test(unittest.TestCase):
	def test_calculate_power_consumption(self):
		f = open("test_input.txt", "r")
		test_input = f.read().splitlines()
		self.assertEqual(calculate_power_consumption(test_input), 198, "Correct product")
		f.close()

if __name__ == "__main__":
	unittest.main()
