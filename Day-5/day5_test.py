#!/usr/bin/python3

from day5_p2 import * 
import unittest

class Test(unittest.TestCase):
	def test_generate_diagonal_coordinates(self):
		self.assertEqual(calculate_overlap(get_start_and_end_coordinates("test_input.txt")), 12, "Correct answer")

	
if __name__ == '__main__':
	unittest.main()
