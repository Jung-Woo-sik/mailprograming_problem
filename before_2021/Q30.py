#Convert a given integer array into a balanced binary search tree

class Node: 
	def __init__(self, d): 
		self.data = d 
		self.left = None
		self.right = None

def arrayToBST(arr): 
	if not arr: 
		return None

	mid = (len(arr)) / 2

	root = Node(arr[mid])  
	root.left = arrayToBST(arr[:mid])
	root.right = arrayToBST(arr[mid+1:]) 
	return root
