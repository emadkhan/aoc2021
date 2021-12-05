#!/usr/bin/python3

def calculate_overlap(start_and_end_coordinates):
	row_size = 1000
	col_size = 1000
	all_coordinates = generate_all_coordinates(start_and_end_coordinates)
	points_count = [ [0] * col_size for _ in range(row_size)]
	for coordinates in all_coordinates:
		for coordinate in coordinates:
			points_count[coordinate[0]][coordinate[1]] += 1

	result = 0	
	for i in range(0, row_size):
		for j in range(0, col_size):
			if points_count[i][j] > 1:
				result += 1

	return result

def generate_all_coordinates(pairs):
	all_coordinates = []
	for pair in pairs:
		coordinates = []
		is_horizontal_or_vertical = pair[0][0] == pair[1][0] or pair[0][1] == pair[1][1]
		if is_horizontal_or_vertical:
			if pair[0][0] == pair[1][0]:
				if pair[0][1] > pair[1][1]:
					for i in range(pair[0][1], pair[1][1] - 1, -1):
						coordinates.append([pair[0][0], i])
		
				else:
					for i in range(pair[0][1], pair[1][1] + 1):
						coordinates.append([pair[0][0], i])
			if pair[0][1] == pair[1][1]:
				if pair[0][0] > pair[1][0]:
					for i in range(pair[0][0], pair[1][0] - 1, -1):
						coordinates.append([i, pair[0][1]])
				else:
					for i in range(pair[0][0], pair[1][0] + 1):
						coordinates.append([i, pair[0][1]])
					
		# Comment out else branch for Part1 only answer	
		else:
			coordinates.extend(generate_diagonal_coordinates(pair))
		all_coordinates.append(coordinates)

	return all_coordinates
		
def generate_diagonal_coordinates(pair):
	coordinates = []

	x_range_coordinates = None
	y_range_coordinates = None

	if pair[0][0] > pair[1][0]:
		x_range_coordinates = [x for x in range(pair[0][0], pair[1][0] - 1, -1)]
	if pair[0][0] < pair[1][0]:
		x_range_coordinates = [x for x in range(pair[0][0], pair[1][0] + 1)]
	if pair[0][1] > pair[1][1]:
		y_range_coordinates = [y for y in range(pair[0][1], pair[1][1] - 1, -1)]
	if pair[0][1] < pair[1][1]:
		y_range_coordinates = [y for y in range(pair[0][1], pair[1][1] + 1)]
	for i in range(0, len(x_range_coordinates)):
		coordinates.append([x_range_coordinates[i], y_range_coordinates[i]])

	return coordinates	
	


def get_start_and_end_coordinates(filename):
	f = open(filename, "r")
	lines = f.read().splitlines()
	start_and_end_coordinates = []
	for line in lines:
		coordinates = line.split('->')
		start = [int(x) for x in coordinates[0].strip().split(',')]
		end = [int(x) for x in coordinates[1].strip().split(',')]
		start_and_end_coordinates.append([start, end])
	f.close()
	return start_and_end_coordinates
	
if __name__ == '__main__':
	print(calculate_overlap(get_start_and_end_coordinates("input.txt")))
	
