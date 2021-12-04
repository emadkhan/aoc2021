#!/usr/bin/python3

ZERO = '0' 
ONE = '1' 

OXYGEN_RATING_MODE = "OXYGEN"
SCRUBBING_RATING_MODE = "SCRUBBING"

def calculate_power_consumption(readings):
	gamma_rate = ""
	epsilon_rate = "" 

	for bit_index in range(0, len(readings[0])):
		count_zero = 0
		count_one = 0
		for i in range(0, len(readings)):
			bit_reading = readings[i][bit_index]
			if bit_reading == ZERO:
				count_zero += 1
			elif bit_reading == ONE:
				count_one += 1
		
		if count_zero > count_one:
			gamma_rate += ZERO
			epsilon_rate += ONE
		else:
			gamma_rate += ONE
			epsilon_rate += ZERO

	return int(gamma_rate, 2) * int(epsilon_rate, 2)


def calculate_life_support_rating(readings):
	oxygen_rating = calculate_rating(readings.copy(), OXYGEN_RATING_MODE)
	scrubbing_rating = calculate_rating(readings.copy(), SCRUBBING_RATING_MODE)
	
	return int(oxygen_rating, 2) * int(scrubbing_rating, 2)


def calculate_rating(readings, mode):
	bit_index = 0
	while len(readings) > 1:
		readings_by_index = {
			ZERO: [],
			ONE: []
		}

		for i in range(0, len(readings)):
			reading = readings[i]
			bit_reading = reading[bit_index]
			if bit_reading == ZERO:
				readings_by_index[ZERO].append(reading)
			elif bit_reading == ONE:
				readings_by_index[ONE].append(reading)

		bit_1_count = len(readings_by_index[ONE])
		bit_0_count = len(readings_by_index[ZERO])

		if mode == "OXYGEN":
			if bit_1_count > bit_0_count or bit_1_count == bit_0_count:
				readings = readings_by_index[ONE]
			else:
				readings = readings_by_index[ZERO]
		else:
			if bit_0_count < bit_1_count or bit_0_count == bit_1_count:
				readings = readings_by_index[ZERO]
			else:
				readings = readings_by_index[ONE]
			

		bit_index += 1

	return readings[0]
	

if __name__ == "__main__":
	f = open("input.txt", "r")
	readings = f.read().splitlines()
	print("Part 1: {0}, Part 2: {1}".format(calculate_power_consumption(readings), calculate_life_support_rating(readings)))
