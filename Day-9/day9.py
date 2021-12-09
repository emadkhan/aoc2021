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

Part2
====

Output:
	* Find the product of the size of the three largest basins
	* Size of the basin is the number of elements that are part of the basin e.g. [4,3,2] will be size 3 
	
Defining a Basin:
	* Levels of Height 9 do not count as being part of a Basin so they form edges within the Matrix.
	* All other points will always be part of exactly one basin. This means a point cannot be part of > 1 basin.
	* A Basin is like the bottom of a bowl. It's bottom is a low point. And all around it, the height decreases until it reaches that low point.
		* Think of Water flowing. If the height decreases till the low point like 4 -> 3 -> 2 -> 1 then water can flow.
		* But if the height decrease is interrupted then water doesn't flow like 4 -> 3 -> 4 -> 2 -> 1
	* A Basin however, is not just radial to the low point. It includes winding channels. 

Insights:
	* Number of Low Points = Number of Basins

Ideas:
	* We want the size of the basin and when writing an algorithm we may report duplicate coordinates.
		* So perhaps we can track a Set of Coordinate pairs which will take care of deduplication for us
	* A Low Point is a Basin of Size 1. This can be a Base case
	* Because we are told that a Point can only be part of 1 basin, when running the algorithm, we can prune execution?


Algorithm:
	* From Part1 we can find out where the low points are. These can anchor the start of the Part2 algorithm.

Recursion Algo:
	* if EXPLORED or DECREASED or NINE or OUT OF BOUNDS then return 0
	* return 1 + go_left + go_right + go_up + go_down

Questions:
	* How to handle duplication?
		* We can keep track of which positions have been explored
		* Or, instead of recursion to count, we can have the recursion build up a set of coordinates so that
			* insertion into the set will take care of deduping. This way, the final operation will just be a len

"""

HIGHEST_POSSIBLE_VALUE = 9
LOWEST_POSSIBLE_VALUE = 0


#Part 1
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

#Part 2
def multiply_three_largest_basins(input):
	basin_sizes = []
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
				basin_sizes.append(measure_basin(i, j, -1, input, set()))

	return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]
	

def measure_basin(x, y, prev, input, explored):
	# Out of Bounds
	if x < 0 or y < 0 or x == len(input) or y == len(input[x]):
		return 0
	
	# Already counted	
	if (x, y) in explored:
		return 0
	
	# 9 is edge of Basin
	if input[x][y] == 9:
		return 0
	
	# Decreased is invalid
	if input[x][y] < prev:
		return 0

	explored.add((x,y))

	go_left = measure_basin(x - 1, y, input[x][y], input, explored)
	go_right = measure_basin(x + 1, y, input[x][y], input, explored)
	go_up = measure_basin(x, y + 1, input[x][y], input, explored)
	go_down = measure_basin(x, y - 1, input[x][y], input, explored)
	
	return 1 + go_left + go_right + go_up + go_down
	 
def parse_input(filename):
	f = open(filename, 'r')
	parsed = [[int(x) for x in list(line)] for line in f.read().splitlines()]
	return parsed

if __name__ == '__main__':
	input = parse_input('test_input.txt')

	print(multiply_three_largest_basins(input))


