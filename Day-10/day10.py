#!/usr/bin/python3

import math

CHUNKS = [('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')]
CORRUPTION_SCORE = {')': 3, ']': 57, '}': 1197, '>': 25137}
COMPLETION_SCORE = {')': 1, ']': 2, '}': 3, '>': 4}

def calculate_score_part_1(input):
	chunks_open_ref = {}
	chunks_close_ref = {}

	for chunk in CHUNKS:
		chunks_open_ref[chunk[0]] = chunk[1]
		chunks_close_ref[chunk[1]] = chunk[0]

	result = 0
	
	for line in input:
		stack = []
		for char in line:
			if char in chunks_open_ref:
				stack.append(char)
			if char in chunks_close_ref:
				to_close = stack.pop()
				if chunks_close_ref[char] != to_close:
					result += CORRUPTION_SCORE[char]
					break
					
				
	return result

def calculate_score_part_2(input):
	chunks_open_ref = {}
	chunks_close_ref = {}

	for chunk in CHUNKS:
		chunks_open_ref[chunk[0]] = chunk[1]
		chunks_close_ref[chunk[1]] = chunk[0]

	scores = []	
	
	for line in input: 
		stack = []
		score = 0
		corrupt = False
		for char in line:
			if char in chunks_open_ref:
				stack.append(char)
			if char in chunks_close_ref:
				to_close = stack.pop()
				if chunks_close_ref[char] != to_close:
					corrupt = True
					break
		
		if corrupt or len(stack) == 0:
			continue
		
		for i in range(len(stack) - 1, -1, -1):
			score *= 5
			score += COMPLETION_SCORE[chunks_open_ref[stack[i]]]
			
		scores.append(score)

	scores.sort()	
	return scores[math.floor(len(scores) / 2)]

def parse_input(filename):
	f = open(filename, 'r')
	parsed = [list(x) for x in f.read().splitlines()]
	return parsed
	

if __name__ == '__main__':
	input = parse_input('input.txt')	
	print(calculate_score_part_2(input))



