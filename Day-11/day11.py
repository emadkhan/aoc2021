#!/usr/bin/python3

def simulate_p1(input, steps):
	flashes = 0
	for n in range(0, steps):
		step_flashes = 0
		for i in range(0, len(input)):
			for j in range(0, len(input[i])):
				input[i][j] += 1
		
		flashed = set()

		for i in range(0, len(input)):
			for j in range(0, len(input[i])):
				if input[i][j] > 9:
					step_flashes += flash_and_cascade(input, i, j, flashed) 
		
		flashes += step_flashes
	
	return flashes
					
def simulate_p2(input):
	target = len(input) * len(input[0])	

	step = 0
	while True:
		step_flashes = 0
		for i in range(0, len(input)):
			for j in range(0, len(input[i])):
				input[i][j] += 1
		
		flashed = set()

		for i in range(0, len(input)):
			for j in range(0, len(input[i])):
				if input[i][j] > 9:
					step_flashes += flash_and_cascade(input, i, j, flashed)

		if step_flashes == target:
			return step + 1
		
		step += 1		
		
def flash_and_cascade(input, x, y, flashed):
	if x == - 1 or x == len(input) or y == -1 or y == len(input[x]):
		return 0

	if (x, y) in flashed:
		return 0

	input[x][y] += 1
	
	if input[x][y] < 10:
		return 0

	flashed.add((x, y))

	flash_left = flash_and_cascade(input, x - 1, y, flashed)
 
	flash_right = flash_and_cascade(input, x + 1, y, flashed)
 
	flash_up = flash_and_cascade(input, x, y + 1, flashed)
 
	flash_down = flash_and_cascade(input, x, y - 1, flashed)
 
	flash_diag_up_right = flash_and_cascade(input, x + 1, y - 1, flashed)
 
	flash_diag_up_left = flash_and_cascade(input, x - 1, y - 1, flashed)
 
	flash_diag_down_right = flash_and_cascade(input, x + 1, y + 1, flashed)
 
	flash_diag_down_left = flash_and_cascade(input, x - 1, y + 1, flashed)
 

	flashes = 1 + flash_left + flash_right + flash_up + flash_down + flash_diag_up_right + flash_diag_up_left + flash_diag_down_right + flash_diag_down_left
		
	input[x][y] = 0

	return flashes	
	
def parse_input(filename):
	f = open(filename, 'r')
	input = [[int(y) for y in list(x)] for x in f.read().splitlines()]
	
	return input


if __name__ == '__main__':
	input = parse_input('input.txt')
	print(simulate_p2(input))
	
