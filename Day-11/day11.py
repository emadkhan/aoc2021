#!/usr/bin/python3

"""

Notes:
	* Output - Total Flashes after 100 steps
	* Input - 2d array with the each element being the energy level
	* Input - 100 elements in a 10x10 2d array
	* Input - Energy levels >= 0 and <= 9
	* R0 - Run n steps
	* R1 - With each step, every element's energy level is incremented
	* R2 - When an element reaches 10, it Flashes and goes back to 0
	* R3 - An Element can only Flash once per step
	* R4 - Flash of an Element causes an increment of Adjacent and Diagonal elements as well
	* R5 - If a FLash causes an Adjacent Flash then this can cause Cascading Flashes
	* R6 - Given an nth step, if cascading flashes occur then the Matrix has changed even before n+1 runs.

Algo:
	* For n in N steps, iterate through each step
	* For nth step, increment element.
	* If element > 9, then call flash() on adjancent and diagonal elements.
	* flash()
		* if element is Out of Bounds, then skip
		* if element is already 10 then skip
		* if element is < 10 then skip
		* else increment this element and flash adjacent and diagonal 
"""

def simulate(input, steps):
	flashes = 0
	for n in range(0, steps):
		for i in range(0, len(input)):
			for j in range(0, len(input[i])):
				input[i][j] += 1
		
		flashed = set()

		for i in range(0, len(input)):
			for j in range(0, len(input[i])):
				if input[i][j] > 9:
					flashes += flash_and_cascade(input, i, j, flashed) 
	
	return flashes
					
		
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
	print(simulate(input, 100))
	
