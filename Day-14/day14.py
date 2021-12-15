#!/usr/bin/python3

import math
			
def solve(template, rules, steps):
	polymer = {}
	for i in range(0, len(template) - 1):
		if template[i] + template[i + 1] not in polymer:
			polymer[template[i] + template[i + 1]] = 0
		polymer[template[i] + template[i + 1]] += 1
		
	for step in range(0, steps):
		counts = {}
		#print("Polymer", polymer)
		for pair in polymer.keys():
			first = pair[0] + rules[pair]		
			second = rules[pair] + pair[1]
			if first not in counts:
				counts[first] = 0
			if second not in counts:
				counts[second] = 0
			counts[first] += polymer[pair]
			counts[second] += polymer[pair]
		polymer = counts

	letter_counts = {}
	
	for pair in polymer.keys():
		first_letter = pair[0]
		second_letter = pair[1]	
		if first_letter not in letter_counts:
			letter_counts[first_letter] = 0
		if second_letter not in letter_counts:
			letter_counts[second_letter] = 0
		letter_counts[first_letter] += polymer[pair]
		letter_counts[second_letter] += polymer[pair]

	for key in letter_counts:
		letter_counts[key] = letter_counts[key]/2	

	a = sorted(list(letter_counts.values()))
	return math.floor(a[-1] - a[0])

def parse_input(filename):
	f = open(filename)
	input = f.read().splitlines()
	template = input[0]
	rules_array = [(x.split(' -> ')[0], x.split(' -> ')[1]) for x in input[2:]]
	rules = {}
	loops = []
	for rule in rules_array:
		rules[rule[0]] = rule[1]
	for rule in rules_array:
		if rules[rule[0][0] + rule[1]] == rule[0][1]:
			loops.append(rule)
	#print(loops)	
	#print(rules)	
	f.close()
	return (template, rules) 

if __name__ == '__main__':
	#input = parse_input('test_input.txt')
	input = parse_input('input.txt')
	print("Running")
	print(solve(input[0], input[1], 40))
