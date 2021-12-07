#!/usr/bin/python3

from linked_list import * 

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
	print(model_growth(input, 80))
	


 
