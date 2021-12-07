#!/usr/bin/python3

from linked_list import * 

def model_growth_2(colony, days):
	# I didn't figure this out myself. Didn't have the buckets insight. Copied from 
	# https://github.com/mahakaal/adventofcode/blob/main/2021/day6/day6.py
	
	age_count_buckets = [colony.count(age) for age in range(9)]
	while days > 0:
		zero_age_count = age_count_buckets[0]
		age_count_buckets[:-1] = age_count_buckets[1:]
		age_count_buckets[6] += zero_age_count
		age_count_buckets[8] = zero_age_count
		days -= 1
	return sum(age_count_buckets)


def model_growth(colony, days):
	colony_list = LinkedList()
	for entry in colony:
		colony_list.add_to_tail(Node(entry))	

	while days > 0:
		curr_size = len(colony_list)
		node = colony_list.get_head()
		while curr_size > 0 and node != None:
			node.set_val(node.get_val() - 1)
			if node.get_val() == -1:
				node.set_val(6)
				colony_list.add_to_tail(Node(8))
			curr_size -= 1
			node = node.get_next()
		#print("")
		#print(colony_list)
		days -= 1

	return len(colony_list)	

def parse_input(filename):
	f = open(filename, "r")
	result = [int(x) for x in f.read().splitlines()[0].split(',')]
	f.close()
	return result

if __name__ == "__main__":
	input = parse_input("input.txt")
	print(model_growth_2(input, 256))
	


 
