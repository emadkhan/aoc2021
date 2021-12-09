#!/usr/bin/python3

"""

Part1
=====

Output:
	* Sum of all risk levels where risk level = low point + 1

Input:
	* We are told 9 is the highest value and 0 is the lowest value


Notes:
	* Given a 2d array of values, find all the numbers where that number is less than its adjacent numbers
	* An adjacent number is horizontally and vertically adjacent.
	* If a number has an adjacent that is lower, then it is not picked. But if there is none lower around it, then it is picked.

Algorithm:
	* Construct a 2d array.
	* Iterate through the array row wise
	* For each element in the array, inspect its adjacent elements
	* Take care of edge elements
	* If an element is the low point, then add 1 and add it to a running sum of risk levels
	* Return sum of risk levels
"""

HIGHEST_POSSIBLE_VALUE = 9
LOWEST_POSSIBLE_VALUE = 0


def calculate_sum_of_risk_levels(input):
	sum_of_risk_levels = 0	
	for i in range(len(input)):
		for j in range(len(input[i])):
			upper = HIGHEST_POSSIBLE_VALUE + 1
			lower = HIGHEST_POSSIBLE_VALUE + 1
			right = HIGHEST_POSSIBLE_VALUE + 1
			left = HIGHEST_POSSIBLE_VALUE + 1
			if i - 1 > -1:
				upper = input[i - 1][j]
			if i + 1 < len(input):
				lower = input[i + 1][j]
			if j - 1 > -1:
				left = input[i][j - 1]
			if j + 1 < len(input[i]):
				right = input[i][j + 1]
			curr = input[i][j]
			if curr < upper and curr < lower and curr < right and curr < left:
				sum_of_risk_levels += curr + 1
	return sum_of_risk_levels

def parse_input(filename):
	f = open(filename, 'r')
	parsed = [[int(x) for x in list(line)] for line in f.read().splitlines()]
	return parsed

if __name__ == '__main__':
	input = parse_input('input.txt')

	print(calculate_sum_of_risk_levels(input))


