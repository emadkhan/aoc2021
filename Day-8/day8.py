#!/usr/bin/python3

import string


"""

Distilled:
	* Seven segment display is used to display one digit
	* ? What is the four digit display ?
	* The seven segments are labeled a-g. When a is turned on, the top line segment is drawn with all a's
	* Complication: Signals wires a-g would correspond to segment lines a-g being turned on but they are mixed up
		* So instead of relying on signal wire a, you must instead work backwards from what you know about how digits are constructed
		* using the number of line segments
	* Complication: Even if you figured out how one wire-signal is scrambled for one 4 digit display, each display is uniquely scrambled
		* However, within one 4 digit display they are consistent in how they are scrambled
	* If wire signal b/g are turned on it doesn't mean line segment b/g are meant to be turned on. You know that the number 1 uses 2 line segments			* So it is more likely that c/f was meant to be turned on. But even if you know its 1, you don't know if b maps to c or f and same for g	* There are 10 unique signal patterns corresponding to digits 0-9
	* The input is 10 observations of signal patters, a | delimetter and then

Insight:
	* Remember, its not the actual letters that matter, its the number of letters. When you see 'gc' or 'cg', because these are 2 letters, they
		* must be actually trying to render 'cf' which is the digit 1

Part 2

Insights
	* Need to take advantage of the fact that 1,4,7,8 have unique counts.
		* This means that 1 is usually c,f but if for a line we see ab then we know that a is either c or f
		* We just need more clues to dial it in
	* 4 is the only number aside from 1 which doesn't have top line

Steps
	* Get top line from 1-7
	* Get bottom line by adding top line to 4. Then find all the segments that have length of 6. Find the one which has only
		* one letter different from your 4 + bottom. The differnce between these is the bottom line. And this segment is 9

Rough
	* Top line = 1 - 7
	* Top Right line = 5 - 9
	* Top Left line = (3 + bottom_left) - 8
	* Center line = 0 - 8
	* Bottom Left line = 8 - 9
	* Bottom Right line = (4 + top + bottom) - 3
	* Bottom line = (4 + (1-7)) - 9

Rough
	* The difference between 4 (bcdf) and 7 (acf) gives you left line and center but you dont know which is which (bd)
	* 4 + 7 segments gives you an almost 9. All you are missing is the bottom line 
	

Questions
	* ??? How do we figure out the mapping ???
	* ? How do we even represent the mapping?


"""

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

	#TODO change loop len
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
		
