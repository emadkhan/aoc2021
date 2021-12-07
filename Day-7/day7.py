#!/usr/bin/python3

def calculate_cost(positions):
	cheapest = -1
	for i in range(0, max(positions) + 1):
		cost = 0
		for j in range(0, len(positions)):
			#move_cost = sum([x for x in range(1, abs(i - positions[j]) + 1)])
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
	parsed = [int(x) for x in f.read().splitlines()[0].split(',')]
	f.close()
	return parsed

if __name__ == '__main__':
	positions = parse_input("input.txt")
	print(calculate_cost(positions))
