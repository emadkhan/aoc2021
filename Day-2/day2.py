#!/usr/bin/python3

FORWARD = 'forward'
DOWN = 'down'
UP = 'up'

def execute_move(instructions):
	forward = 0
	depth = 0
	for i in range(0, len(instructions), 2):
		instruction = instructions[i]
		measurement = int(instructions[i + 1])
		if instruction == FORWARD:
			forward += measurement
		elif instruction == DOWN:
			depth += measurement
		elif instruction == UP:
			depth -= measurement
			
	return forward * depth

def execute_move_with_aim(instructions):
	forward = 0
	depth = 0
	aim = 0
	for i in range(0, len(instructions), 2):
		instruction = instructions[i]
		measurement = int(instructions[i + 1])
		if instruction == FORWARD:
			forward += measurement
			depth += measurement * aim
		elif instruction == DOWN:
			aim += measurement
		elif instruction == UP:
			aim -= measurement
			
	return forward * depth

if __name__ == "__main__":
	f = open('input.txt', 'r')
	instructions = f.read().split()
	print("Part1: {0}, Part2: {1}".format(execute_move(instructions), execute_move_with_aim(instructions)))
