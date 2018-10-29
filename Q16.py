#binary tree parsing

def solution(root):
	forward = [root]
	backward = []

	while backward or forward:
		while forward:
			tmp = forward.pop()
			print(tmp.data)

			if tmp.left:
				backward.append(tmp.left)
			if tmp.right:
				backward.append(tmp.right)

		while backward:
			tmp = backward.pop()
			print(tmp.data)

			if tmp.right:
				forward.append(tmp.right)
			if tmp.left:
				forward.append(tmp.left)


