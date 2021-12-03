#!/usr/bin/python3

"""
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
	epsilon_rate = "" # We can actually just record the gamma rate and have the epsilon rate be the flipped bit

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
	print("Gamma Rate: {0}, Epsilon Rate: {1}".format(gamma_rate, epsilon_rate))

	return int(gamma_rate, 2) * int(epsilon_rate, 2)

			

if __name__ == "__main__":
	f = open("input.txt", "r")
	readings = f.read().splitlines()
	print(calculate_power_consumption(readings))
