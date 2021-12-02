#!/usr/bin/python3

from day2 import * 
import unittest

class TestSum(unittest.TestCase):

	def test_empty(self):
		self.assertEqual(execute_move([]), 0, "Should be 0 for empty list")
	
	def test_no_depth_changes(self):
		self.assertEqual(execute_move(['forward', '5']), 0, "Should be 0 for no depth changes")
	
	def test_forward_and_depth(self):
		self.assertEqual(execute_move(['forward', '5', 'down', '5', 'forward', '8', 'up', '3', 'down', '8', 'forward', '2']), 150, "Should produce product of forward and depth changes")

	def test_forward_and_depth_with_aim(self):
		self.assertEqual(execute_move_with_aim(['forward', '5', 'down', '5', 'forward', '8', 'up', '3', 'down', '8', 'forward', '2']), 900, "Should produce product of forward and depth changes")

if __name__ == '__main__':
	unittest.main()
