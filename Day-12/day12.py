#!/usr/bin/python3

def parse_input(filename):
	f = open(filename)
	input = f.read().splitlines()
	f.close()
	return input

if __name__ == '__main__':
	#input = parse_input('test_input.txt')
	input = parse_input('input.txt')
	print("Running")
