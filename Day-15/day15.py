#!/usr/bin/python3

"""

Notes:
	* Input - Parse into a 2d array of rows and cols. Each entry is >= 1 and <= 9.
	* Rule - Only count an element if its entered. Starting position does not count as you begin there.
	* Rule - Start in the top left
	* Rule - Cannot move diagonally
	* Output - Find path with the lowest total sum from Top Left to Bottom Right.

Insights:
	* We only need the total for the result, we do not need to know what the path we take is
	* We do not want to reenter a position as that is duplication wasteful
	* You have to watch out for making a locally optimal but globally sub-optimal decision.
	* If I remember correctly, the bottoms up dynamic programming approach builds the sum at each position
		 and progresses towards the target. So [0,0] would be 0 [0,1] would be 2, then [0, 2] would be 8 and
		and [0, 3] would be 11.	
	* For Top Down dynamic programming, the decisions are:
		* go right
		* go left
		* go up
		* go down
"""

MAX = 10

def solve_bottoms_up(input):
	traversed = [[0] * len(input[0]) for x in range(0, len(input))]
	for i in range(0, len(input)):
		for j in range(0, len(input[i])):
			if i == 0 and j == 0:
				traversed[i][j] == input[i][j]
			elif i == 0:
				traversed[i][j] = input[i][j] + traversed[i][j - 1]
			elif j == 0:
				traversed[i][j] = input[i][j] + traversed[i - 1][j]
			else:
				traversed[i][j] = input[i][j] + min(traversed[i - 1][j], traversed[i][j - 1])
	return traversed[-1][-1]

# TODO: This doesn't work. Why?
def solve_top_down(input, i, j, traversed):
	if i == -1 or j == -1 or i == len(input) or j == len(input[i]):
		return MAX
	if i == len(input) - 1 and j == len(input[i]) - 1:
		print(">>>>>>>>>>>>>>>>> END >>>>>>>>>>>>")
		return input[i][j]
	if (i, j) in traversed:
		return MAX
	traversed.append((i, j))
	go_right = solve(input, i, j + 1, traversed)
	go_left = solve(input, i, j - 1, traversed)
	go_up = solve(input, i - 1, j, traversed)
	go_down = solve(input, i + 1, j, traversed)
	print(traversed)	
	total = input[i][j] + min(go_right, go_left, go_up, go_down)
	traversed.pop()
	return total
		
def parse_input(filename):
	f = open(filename)
	input = f.read().splitlines()
	parsed = [[int(y) for y in list(x)] for x in input]
	#parsed = [[1, 1, 6, 3], [1, 3, 8, 1], [2, 1, 3, 6]]
	#parsed = [[3, 8, 1], [1, 3, 6]]
	f.close()
	return parsed 

if __name__ == '__main__':
	#input = parse_input('test_input.txt')
	input = parse_input('larger_input.txt')
	print("Running")
	print(solve_bottoms_up(input))
	
