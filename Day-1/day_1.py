#!/bin/python

def count_increases(readings):
	if len(readings) < 2:
		return 0

	prev_reading = readings[0]
	increases_count = 0

	for i in range(1, len(readings)):
		if readings[i] > prev_reading:
			increases_count += 1
		prev_reading = readings[i]

	return increases_count	


def count_sliding_window_increases(readings):
	if len(readings) < 4:
		return 0

	prev_sum = readings[0] + readings[1] + readings[2]
	increases_count = 0

	for i in range(1, len(readings) - 2):
		curr_sum = readings[i] + readings[i + 1] + readings[i + 2]
		if curr_sum > prev_sum:
			increases_count += 1
		prev_sum = curr_sum
		
	return increases_count	
	
	

if __name__ == "__main__":
	f = open('input.txt', 'r')
	readings = [ int(x) for x in f.read().split() ]
	print("Part 1:{0}, Part 2:{1}".format(count_increases(readings), count_sliding_window_increases(readings)))




