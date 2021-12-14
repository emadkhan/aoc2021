#!/usr/bin/python3

"""
Notes:
	* Output - After running 10 steps, what is the count of most common element minus least common element
	* Input - First line is the starting string
	* Input - Then you have insertion rules
	* Input - In the starting string, two letters form a pair and each pair has some insertion rule about what to insert
		in between them.
	* Rule - All pair insertions happen simulatenously for an iteration. If you start with NNCB then after inserting for 
		NN, the next pair is still NC even if something got inserted in between NN like A so its not AN
"""

def solve_part1(template, rules, steps):
	polymer = template
	for step in range(0, steps):
		new_polymer = "" 
		for i in range(0, len(polymer)):
			if i == len(polymer) - 1:
				new_polymer += polymer[i]
			else:
				new_polymer += polymer[i] + rules[polymer[i] + polymer[i + 1]]
		polymer = new_polymer
	

	counts = {}
	for letter in polymer:
		if letter not in counts:
			counts[letter] = 0
		counts[letter] += 1
	counts_sorted = list(counts.values())
	counts_sorted.sort()
	return counts_sorted[-1] - counts_sorted[0]
			
def parse_input(filename):
	f = open(filename)
	input = f.read().splitlines()
	template = input[0]
	rules_array = [(x.split(' -> ')[0], x.split(' -> ')[1]) for x in input[2:]]
	rules = {}
	for rule in rules_array:
		rules[rule[0]] = rule[1]	
	
	f.close()
	return (template, rules) 

if __name__ == '__main__':
	#input = parse_input('test_input.txt')
	input = parse_input('input.txt')
	print("Running")
	print(solve_part1(input[0], input[1], 10))
