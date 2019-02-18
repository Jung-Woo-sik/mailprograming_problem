#Given a singly linked list, print the value of the node that is in the middle of the list.

class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next 

# node1 -> node2 -> node3 -> node4 -> node5 -> None
node5 = Node("e", None)  
node4 = Node("d", node5)
node3 = Node("c", node4) 
node2 = Node("b", node3)
node1 = Node("a", node2)  

head = node1

fastPointer = head
slowPointer = head

while fastPointer.next != None and fastPointer.next.next != None:
	fastPointer = fastPointer.next.next
	slowPointer = slowPointer.next

print (slowPointer.data)
