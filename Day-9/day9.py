#!/usr/bin/python3

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
				basin_sizes.append(measure_basin(i, j, LOWEST_POSSIBLE_VALUE - 1, input, set()))

	basin_sizes.sort()
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
	input = parse_input('input.txt')

	print(multiply_three_largest_basins(input))


