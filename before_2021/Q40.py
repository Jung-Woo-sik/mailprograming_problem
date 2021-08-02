#doubly linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class LinkedList:
	def __init__(self):
		self.head = None

	def add(self, data):
		node = Node(data)
		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			node.next.prev = node
			self.head = node
	def search(self, k):
		p = self.head
		if p != None:
			while p.next != None:
				if p.data == k:
					return p
				p = p.next
				if p.data == k:
					return p
		return None

	def remove(self, p):
		tmp = p.prev
		p.prev.next = p.next
		p.prev = tmp

