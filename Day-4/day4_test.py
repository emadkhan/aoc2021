#!/usr/bin/python3

from day4_part2 import * 
import unittest

class TestSum(unittest.TestCase):
	def test_calculate_power_consumption(self):
		input = get_draws_and_boards("test_input.txt")
		self.assertEqual(calculate_final_score(input[0], input[1]), 1924, "Correct product")
	
if __name__ == '__main__':
	unittest.main()
