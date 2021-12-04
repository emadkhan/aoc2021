#!/usr/bin/python3

from day4 import * 
import unittest

class Test(unittest.TestCase):
	def test_part_1(self):
		input = get_draws_and_boards("test_input.txt")
		self.assertEqual(calculate_final_score(input[0], input[1])['Part1']['result'], 4512, "Correct product")
	def test_part_2(self):
		input = get_draws_and_boards("test_input.txt")
		self.assertEqual(calculate_final_score(input[0], input[1])['Part2']['result'], 1924, "Correct product")
	
if __name__ == '__main__':
	unittest.main()
