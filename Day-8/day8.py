#!/usr/bin/python3

import string

DIGIT_MAP = {
	0: 'abcefg',
	1: 'cf',
	2: 'acdeg',
	3: 'acdfg',
	4: 'bcdf',
	5: 'abdfg',
	6: 'abdefg',
	7: 'acf',
	8: 'abcdefg',
	9: 'abcdfg'
}

def count_digits_part_2(readings):
	sum = 0	
	DIGIT_LEN_LOOKUP = {}
	DIGIT_MAP_REVERSE = {}

	for key in DIGIT_MAP:
		DIGIT_LEN_LOOKUP[len(DIGIT_MAP[key])] = key
		DIGIT_MAP_REVERSE[''.join(sorted(DIGIT_MAP[key]))] = key

	for reading in readings:
		known_digits = {}
		new_mappings = {}
		for letter in string.ascii_lowercase[:7]:
			new_mappings[letter] = None
		points = reading[0]
		output_values = reading[1]
		length_six = []
		length_five = []
		for point in points:
			digit = DIGIT_LEN_LOOKUP[len(point)]
			if digit in [1,4,7,8]:
				known_digits[digit] = set(point)
			if len(point) == 6:
				length_six.append(point)
			if len(point) == 5:
				length_five.append(point)

		# Set Top 'a'		
		new_mappings['a'] = (set(known_digits[7]) - set(known_digits[1])).pop()

		# Set Bottom 'g'
		for entry in length_six:
			maybe_bottom = set(entry) - (set(known_digits[7]) | set(known_digits[4]))
			if len(maybe_bottom) == 1:
				new_mappings['g'] = maybe_bottom.pop()
				# We are looking at 9 digit
				known_digits[9] = set(entry)
				

		# Set Bottom Left 'e'
		new_mappings['e'] = (known_digits[8] - (set(known_digits[7]) | set(known_digits[4]) | set(new_mappings['g']))).pop()


		# Set Top Left 'b'
		for entry in length_six:
			maybe_top_left = set(entry) - (known_digits[7] | set(new_mappings['e']) | set(new_mappings['g']))
			# We are looking at 0 digit
			if len(maybe_top_left) == 1:
				known_digits[0] = set(entry)
				for elem in maybe_top_left:
					new_mappings['b'] = elem

				# Set Center 'd'
				new_mappings['d'] = (known_digits[8] - set(entry)).pop()
		# Set Top Right 'c'
		for entry in length_five:
			entry_set = set(entry)
			if new_mappings['b'] in entry_set and new_mappings['e'] not in entry_set:
				# We are looking at 5 digit
				known_digits[5] = entry
				# Add bottom left to 5 and then subtract from 8 to get top right
				new_mappings['c'] = (known_digits[8] - (set(entry) | set(new_mappings['e']))).pop()
		
		# Set Bottom Right 'f'
		# At this point, what ever letter is left is going to be bottom right
		
		new_mappings['f'] = (set(string.ascii_lowercase[:7]) - set(list(new_mappings.values()))).pop()
		

		new_mappings_reverse = {}
		for key in new_mappings:
			new_mappings_reverse[new_mappings[key]] = key
		# Calculate Output
		decoded_digit = ''
		for output_value in output_values:
			decoded_output = ''	
			for letter in output_value:
				decoded_output += new_mappings_reverse[letter]
			decoded_digit += str(DIGIT_MAP_REVERSE[''.join(sorted(decoded_output))])

		sum += int(decoded_digit)
	return sum
			
	

def count_digits_part_1(readings):
	count = 0
	DIGIT_LEN_LOOKUP = {}
	for key in DIGIT_MAP:
		DIGIT_LEN_LOOKUP[len(DIGIT_MAP[key])] = key
	for reading in readings:
		output = reading[1]
		for segments in output:
			digit = DIGIT_LEN_LOOKUP[len(segments)]
			if digit in [1,4,7,8]:
				count += 1
	
	return count

def parse_input(filename):
	f = open(filename, 'r')
	lines = f.read().splitlines()
	parsed = []
	for line in lines:
		line_split = line.split('|')
		parsed.append((line_split[0].split(), line_split[1].split()))
	return parsed

if __name__ == '__main__':
	readings = parse_input("input.txt")
	print(count_digits_part_2(readings))
		
