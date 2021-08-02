#Given two integers represented as linked lists, return a linked list that is a sum of the two given linked lists.

def addTwoLinkedLists(result, A, B): 
	prev = None
	temp = None
	carry = 0 # 받아올림 

	while(A is not None or B is not None): 
		A_value = 0 if A is None else A.data 
		B_value = 0 if B is None else B.data

# 저번 루프의 받아올림 + A리스트 노드값 + B리스트 노드값
		Sum = carry + A_value + B_value 
		carry = 0
		if (Sum >= 10) {
			carry = 1
			Sum = Sum % 10
		}

		temp = Node(Sum) 

		if result.head is None: 
			result.head = temp 
		else : 
			prev.next = temp

# 다음번의 덧셈을 위해 전값을 저장시켜놓습니다.
		prev = temp 

# 두 노드를 전진 시킵니다. 
		if A is not None: 
			A = A.next
		if B is not None: 
			B = B.next

# 두 리스트 모두 끝을 보았을때 받아올림이 있다면 마지막 노드를 만들어 줍니다. 
	if carry > 0: 
		temp.next = Node(carry)
