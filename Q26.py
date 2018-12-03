def Recurse(node, x, y): 
	if node is None: 
		return 

	if x < node.data : 
		Recurse(node.left, x, y) 
	  
	if x <= node.data and y >= node.data: 
		print node.data, 
				  
	if y > node.data: 
		Recurse(node.right, x, y) 
