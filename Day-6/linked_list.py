class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def __iter__(self):
		node = self.head
		while node is not None:
			yield node
			node = node.next

	def __repr__(self):
		nodes = []
		for node in self:
			nodes.append(str(node.get_val()))
		return " -> ".join(nodes)

	
	def __len__(self):
		return self.size

	def get_head(self):
		return self.head

	def add_to_tail(self, node):
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			self.tail.set_next(node)
			self.tail = node

		self.size += 1

	

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

	def set_next(self, node):
		self.next = node

	def __repr__(self):
		return self.val

	def get_val(self):
		return self.val

	def set_val(self, val):
		self.val = val

	def get_next(self):
		return self.next


