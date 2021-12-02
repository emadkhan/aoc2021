#!/bin/python

def count_increases(readings):
	if len(readings) < 2:
		return 0

	prev_reading = readings[0]
	increases_count = 0

	for i in range(1, len(readings)):
		if readings[i] > prev_reading:
			increases_count = increases_count + 1
		prev_reading = readings[i]

	return increases_count	


if __name__ == "__main__":
	f = open('input.txt', 'r')
	readings = f.read().split()
	print(count_increases(readings))



