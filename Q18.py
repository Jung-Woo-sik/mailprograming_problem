# Given a binary tree root node, reverse the tree horizontally.

def invert(root):
	if root == None:
		return None
	right = invert(root.right)
	left = invert(root.left)
	root.left = right
	root.right = left
	return root

