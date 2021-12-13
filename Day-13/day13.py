#!/usr/bin/python3

def solve(dots, folds):
	matrix = create_matrix(dots)
	fill_matrix(matrix, dots)
	for fold in folds:
		if fold[0] == 'x':
			print("Folding x at {}".format(fold[1]))
			matrix = fold_x(matrix, fold[1])	
		elif fold[0] == 'y':
			print("Folding y at {}".format(fold[1]))
			matrix = fold_y(matrix, fold[1])	
	result = 0	
	for row in matrix:
		result += row.count(1)
	letters_matrix = [['.' for x in range(0, len(matrix[0]))] for y in range(len(matrix))]
	for i in range(0, len(matrix)):
		for j in range(0, len(matrix[0])):
			if matrix[i][j] == 1:
				letters_matrix[i][j] = '#'
		
	for row in letters_matrix:
		print(row)
	print("")
	return result
		

def fold_x(matrix, position):
	for y in range(0, len(matrix)):
		for x in range(position + 1, len(matrix[y])):
			if matrix[y][x] == 1:
				matrix[y][2 * position - x] = 1
	
	return [row[:position] for row in matrix]

def fold_y(matrix, position):
	for y in range(position + 1, len(matrix)):
		for x in range(0, len(matrix[y])):
			if matrix[y][x] == 1:
				matrix[2 * position - y][x] = 1

	return matrix[:position]	

def fill_matrix(matrix, dots):
	for dot in dots:
		matrix[dot[1]][dot[0]] = 1	

def create_matrix(dots):
	max_x = 0
	max_y = 0
	for dot in dots:
		max_x = max(dot[0], max_x)
		max_y = max(dot[1], max_y)
	return [[0 for x in range(0, max_x + 1)] for y in range(0, max_y + 1)]

def parse_input(filename):
	f = open(filename)
	input = f.read().splitlines()
	split_point = input.index('')
	dots = [(int(x.split(',')[0]), int(x.split(',')[1])) for x in input[:split_point]]
	folds = [(x.split('=')[0][-1], int(x.split('=')[1])) for x in input[split_point + 1:]]
	
	f.close()
	return (dots, folds) 

if __name__ == '__main__':
	#input = parse_input('test_input.txt')
	input = parse_input('input.txt')
	print(solve(input[0], input[1]))
