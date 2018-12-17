class LinkedList:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

def solution(head):
	start = end = head

	while start:
		end = start
		total = 0
		skip = False

		while end:
			total += end.data
			if total == 0:
				start = end
				skip = True
				break
			end = end.next

		if not skip:
			print(start.data)

		start = start.next

