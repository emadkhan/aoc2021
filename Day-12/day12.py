#!/usr/bin/python3

import string

class Node:
	def __init__(self, data):
		self.data = data
		self.is_large_cave = is_all_upper_case(data)
		self.is_small_cave = not self.is_large_cave
		self.edges = []

	def __str__(self):
		return "Node: {0}. Edges: {1}".format(self.data, [x.data for x in self.edges])
	
	def add_edge(self, node):
		self.edges.append(node)
		

class Graph:
	def __init__(self):
		self.nodes = {}
		self.paths = []

	def __str__(self):
		return ','.join(list(self.nodes.keys()))

	def add_node(self, node):
		self.nodes.append(node)

	def print_paths(self):
		pass
	
	def add_node(self, node):
		self.nodes[node.data] = node

def calculate_paths(input):
	g = create_graph(input)
	start = g.nodes['start']

	for edge in start.edges:
		explore(edge, ['start'], g)
	
	print(len(g.paths))
		

def explore(node, path, g):
	if node.data == 'end':
		path.append(node.data)
		g.paths.append(','.join(path))
		path.pop()
		return
	
	if node.is_small_cave and node.data in path:
		return

	path.append(node.data)
	
	for edge in node.edges:
		explore(edge, path, g)

	path.pop()

	return
		

def create_graph(input):
	g = Graph()
	for entry in input:
		first = None
		second = None

		if entry[0] in g.nodes:
			first = g.nodes[entry[0]]
		else:
			first = Node(entry[0])
			g.add_node(first)
	
		if entry[1] in g.nodes:
			second = g.nodes[entry[1]]
		else:
			second = Node(entry[1])
			g.add_node(second)

		first.add_edge(second)
		second.add_edge(first)	

	return g
		

def is_all_upper_case(input):
	for letter in input:
		if letter not in string.ascii_uppercase:
			return False	
	return True
	

def parse_input(filename):
	f = open(filename)
	input = [(x.split('-')[0], x.split('-')[1]) for x in f.read().splitlines()]
	f.close()
	return input

if __name__ == '__main__':
	input = parse_input('input.txt')
	#input = parse_input('input.txt')
	calculate_paths(input)
	
