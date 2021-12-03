#!/usr/bin/python3

"""
======
PART 1
======

Defining the Problem:

	* The input is binary numbers all of the same binary string length
	* For each column, starting from left to right, calculate the occurences of 0 and 1
	* Once you have this data for a column, the Gamma rate is the most common bit and the Epsilon rate is the least common bit
	* For each column, record the Gamma rate and the Epsilon rate so that by the end you have 2 new binary numbers for Gamma, Epsilon
	* Convert these two numbers to Decimal, multiply them and this is the answer


Options:
	* O(n * m) where n is the size of input and m is the length of each binary reading
"""

def calculate_power_consumption(readings):
	gamma_rate = ""
	epsilon_rate = "" 

	for bit_index in range(0, len(readings[0])):
		count_zero = 0
		count_one = 0
		for i in range(0, len(readings)):
			bit_reading = readings[i][bit_index]
			if bit_reading == '0':
				count_zero += 1
			elif bit_reading == '1':
				count_one += 1
		
		if count_zero > count_one:
			gamma_rate += '0'
			epsilon_rate += '1'
		else:
			gamma_rate += '1'
			epsilon_rate += '0'

	return int(gamma_rate, 2) * int(epsilon_rate, 2)

"""
======
PART 2
======

Defining the Problem

	* Similar to Part1, we need to iterate column wise for a list of input.
	* However, now the input list keeps shrinking
	* For each bit, it branches into two different lines of processing. One for oxygen rating, the other for scrubber rating.
"""

def calculate_life_support_rating(readings):
	oxygen_rating = calculate_rating(readings.copy(), "OXYGEN")
	scrubbing_rating = calculate_rating(readings.copy(), "SCRUBBING")
	print("Oxygen: {0}, Scrubbing: {1}".format(oxygen_rating, scrubbing_rating))
	
	return int(oxygen_rating, 2) * int(scrubbing_rating, 2)


def calculate_rating(readings, mode):
	bit_index = 0
	while len(readings) > 1:
		readings_by_index = {
			"0": [],
			"1": []
		}

		for i in range(0, len(readings)):
			reading = readings[i]
			bit_reading = reading[bit_index]
			if bit_reading == '0':
				readings_by_index['0'].append(reading)
			elif bit_reading == '1':
				readings_by_index['1'].append(reading)

		bit_1_count = len(readings_by_index["1"])
		bit_0_count = len(readings_by_index["0"])

		if mode == "OXYGEN":
			if bit_1_count > bit_0_count or bit_1_count == bit_0_count:
				readings = readings_by_index["1"]
			else:
				readings = readings_by_index["0"]
		else:
			if bit_0_count < bit_1_count or bit_0_count == bit_1_count:
				readings = readings_by_index["0"]
			else:
				readings = readings_by_index["1"]
			

		bit_index += 1

	return readings[0]
	

if __name__ == "__main__":
	f = open("input.txt", "r")
	readings = f.read().splitlines()
	print("Part 1: {0}, Part 2: {1}".format(calculate_power_consumption(readings), calculate_life_support_rating(readings)))
