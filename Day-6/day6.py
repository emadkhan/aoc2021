#!/usr/bin/python3

"""

Part 1

Notes:

	* Goal: After modeling for the growth of an initial state, how many fish would there by after 80 days?
	* Algorithm: Involves going through 80 iterations and for each iteration to modify the population and internal state of each fish.
	* Data Structure: An Array works well because we only ever append to it and each element stays in the array, only its state is modified in place
	* Instruction: New fish is spawned with an internal timer of 8, not 7 because it needs extra time to reproduce
	* Risk: Off by one error. How many iterations of the loop? n or n+1?
"""



def model_growth(colony, days):
	while days > 0:
		# 1. Decrement existing values. Reset value if it is -1
		# 2. For every value that hits zero, add an 8 to the colony
		for i in range(0, len(colony)):
			colony[i] -= 1
			if colony[i] == -1:
				colony[i] = 6
				colony.append(8)
		
		#print("Day {0}: {1}".format(days, colony))
		#print("")
		days -= 1
	return len(colony)	

def parse_input(filename):
	f = open(filename, "r")
	result = [int(x) for x in f.read().splitlines()[0].split(',')]
	f.close()
	return result


if __name__ == "__main__":
	input = parse_input("test_input.txt")
	print(model_growth(input, 256))
	


 
