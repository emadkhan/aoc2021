#!/bin/python3

def execute_move(instructions):
	forward = 0
	depth = 0
	for i in range(0, len(instructions), 2):
		instruction = instructions[i]
		measurement = int(instructions[i + 1])
		if instruction == 'forward':
			forward += measurement
		elif instruction == 'down':
			depth += measurement
		elif instruction == 'up':
			depth -= measurement
			
	return forward*depth

if __name__ == "__main__":
	f = open('input.txt', 'r')
	instructions = f.read().split()
	print(execute_move(instructions))
