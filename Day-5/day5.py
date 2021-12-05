#!/usr/bin/python3

"""
PART 1
Notes:
	* A line segment has a starting coordinate and an ending coordinate and itertes through to draw a line in between the points of the two ends
	* For Part1 only concerned with Horizontal and Vertical Line segments so no diagonals.
	* 

Ideas:
	* Keep a dictionary where the key is a (x, y) coordinate tuple so each time you are processing an input and generating coordinate tuples you can be populating the dictionary


Requirements
	* Parse input - Done
	* Generate all coordinates given start and end coordiantes - Done
	* Populate data structure to record count of occurances and overlaps
	* Iterate through data structure to find all counts > 2
"""

def calculate_overlap(start_and_end_coordinates):
	all_coordinates = generate_all_coordinates(start_and_end_coordinates)
	points_count = [ [0] * 1000 for _ in range(1000)]
	for coordinates in all_coordinates:
		for coordinate in coordinates:
			points_count[coordinate[0]][coordinate[1]] += 1

	result = 0	
	for i in range(0, 1000):
		for j in range(0, 1000):
			if points_count[i][j] > 1:
				result += 1

	return result

def generate_all_coordinates(pairs):
	all_coordinates = []
	for pair in pairs:
		coordinates = []	
		is_horizontal_or_vertical = pair[0][0] == pair[1][0] or pair[0][1] == pair[1][1]
		if not is_horizontal_or_vertical:
			continue
		if pair[0][0] == pair[1][0]:
			pair.sort(key = lambda x:x[1])
		if pair[0][1] == pair[1][1]:
			pair.sort(key = lambda x:x[0])
		if pair[0][0] == pair[1][0]: 
			for i in range(pair[0][1], pair[1][1] + 1):
				coordinates.append([pair[0][0], i])
		if pair[0][1] == pair[1][1]: 
			for i in range(pair[0][0], pair[1][0] + 1):
				coordinates.append([i, pair[0][1]])
		all_coordinates.append(coordinates)
	return all_coordinates
		

def get_start_and_end_coordinates(filename):
	f = open(filename, "r")
	lines = f.read().splitlines()
	start_and_end_coordinates = []
	for line in lines:
		coordinates = line.split('->')
		start = [int(x) for x in coordinates[0].strip().split(',')]
		end = [int(x) for x in coordinates[1].strip().split(',')]
		start_and_end_coordinates.append([start, end])
	return start_and_end_coordinates
	
if __name__ == '__main__':
	print(calculate_overlap(get_start_and_end_coordinates("input.txt")))
	
