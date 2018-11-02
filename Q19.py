def solution(head ,n):
	if (head == null):
		return None
	
	first = head
	second = head

	for i in range(0,n) :
		first = first.next
	if first == None:
		head = head.next
		return head
	while first.next != None:
		first = first.next;
		second = second.next;
	second.next = second.next.next
	return head;
