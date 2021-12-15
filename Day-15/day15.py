#!/usr/bin/python3

from queue import PriorityQueue 

# This is actually incorrect. Works for part 1 but doesn't work for part 1
# Part 1 gets luck with only going right and down.
def solve_part_one(input):
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

def solve(input):
	pq = PriorityQueue()
	pq.put((0, (0,0)))
	visited = {(0,0)}
	while pq:
		risk, (i, j) = pq.get()
		if i == len(input) - 1 and j == len(input[0]) - 1:
			return risk
		neighbours = get_neighbours(input, i, j)
		for neighbour in neighbours:
			if neighbour not in visited:
				pq.put((risk + input[neighbour[0]][neighbour[1]], (neighbour[0], neighbour[1])))
				visited.add(neighbour)
	

def get_neighbours(input, i, j):
	result = []
	if i > 1:
		result.append((i - 1, j))
	if j > 1:
		result.append((i, j - 1))
	if i < len(input) - 1:
		result.append((i + 1, j))
	if j < len(input[i]) - 1:
		result.append((i, j + 1))
	return result
		

def expand_input(input):
	result = []
	for i in range(0, 5):
		to_add = [[y + i if y + i < 10 else (y + i) % 9 for y in x] for x in input]
		for row in to_add:
			result.append(row)
	base_tile = [x.copy() for x in result]
	for idx in range(0, len(base_tile)):
		row = base_tile[idx]
		for i in range(1, 5):
			extend_with = [x + i if x + i < 10 else (x + i) % 9 for x in row]

			result[idx].extend(extend_with)

	return result

def parse_input(filename):
	f = open(filename)
	input = f.read().splitlines()
	parsed = [[int(y) for y in list(x)] for x in input]
	f.close()
	return parsed 

if __name__ == '__main__':
	#input = parse_input('test_input.txt')
	input = parse_input('input.txt')
	print("Running")
	print(solve(expand_input(input)))
