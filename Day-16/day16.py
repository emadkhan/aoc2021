#!/usr/bin/python3

"""

Requirements 
	* Convert Hexadecimal to Binary - Done
	* Convert binary to decimal - done
	* From a packet, get header to decode packet version and packet type id
	* From a packet, get literal value when packet type id is 4
	* >>>>>>>>>> How to know how many bits are useless at the end?

Rules
	* First 3 bits = packet version
	* Next 3 bits = packet type id
	* packet type Id rules
		* 4 represent literal value
		* encodes a single binary number
		* binary number padded with zeros and then broken into groups of 4 bits
		* each group is prefixed by a 1 except last group
		* So these are groups of 5 bits following the packet header

Output:
	* Part 1 - Add up version numbers from all the packets

"""

def convert_binary_to_decimal(input):
	return int(input, 2)

def convert_hex_to_binary(input):
	return bin(int(input, 16))[2:]

def parse_input(filename):
	f = open(filename)
	input = f.read().splitlines()
	f.close()
	print(convert_hex_to_binary(input[0]))


def solve(input):
	version_sum = 0
	index = 0
	while index < len(input) - 6:
		print(input)
		packet_version = convert_binary_to_decimal(input[index:index + 3])
		packet_type_id = convert_binary_to_decimal(input[index + 3: index + 6])
		print("Packet Version: {}".format(packet_version))	
		print("Packet Type Id: {}".format(packet_type_id))	
	
		version_sum += packet_version
		curr = index + 6
	
		if packet_type_id == 4:
			while input[curr] != '0':
				# For Packets starting with 1 bit
				print(input[curr: curr + 5])
				curr += 5
	
				# For Final Packet starting with 0 bit	
				print(input[curr: curr + 5])
				curr += 5
		else:
			length_type_id = input[curr]
			if length_type_id == '0':
				length_in_bits = convert_binary_to_decimal(input[curr:curr + 15])
				print("Length: {}".format(length_in_bits))	
				curr += 15	
			else:
				number_of_packets = convert_binary_to_decimal(input[curr:curr + 11])
				print("Number: {}".format(number_of_packets))	
				curr += 11
		index += curr
				
			
				
	
	
if __name__ == '__main__':
	input = parse_input('test_input.txt')
	#input = parse_input('input.txt')
	print("Running")
	#print(solve(input))
	

	
	
	
