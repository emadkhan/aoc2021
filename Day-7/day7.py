#!/usr/bin/python3

"""
~ time ./day7.py
98925151.0
./day7.py  0.87s user 0.01s system 99% cpu 0.888 total
"""

def calculate_cost(positions):
	cheapest = -1
	for i in range(0, max(positions) + 1):
		cost = 0
		for j in range(0, len(positions)):
			temp = abs(i - positions[j])
			move_cost = (temp**2 + temp) / 2
			cost += move_cost
		if cheapest == -1:
			cheapest = cost
		else:
			cheapest = cost if cost < cheapest else cheapest 
	
	return cheapest	

def parse_input(filename):
	f = open(filename, 'r')
	parsed = [int(x) for x in f.read().split(',')]
	f.close()
	return parsed

if __name__ == '__main__':
	positions = parse_input("input.txt")
	print(calculate_cost(positions))
