#Given a singly linked list L: L0→L1→…→Ln-1→Ln, reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
def solution(self, head):
	if head is None or head.next is None or head.next.next is None:
		return

# 1->2->3->4  =>  1->2, 3->4
	slow=fast=head
	while fast.next and fast.next.next:
		slow=slow.next
		fast=fast.next.next
	head2=slow.next
	slow.next=None

# 3->4  =>  4->3
	temp_head=ListNode()
	temp_head.next=head2
	p=head2.next
	head2.next=None
	while p:
		tmp=p
		p=p.next
		tmp.next=temp_head.next
		temp_head.next=tmp
	head2=temp_head.next

# 1->2, 4->3  =>  1->4->2->3
	p1=head
	p2=head2
	while p2:
		t1=p1.next
		p1.next=p2
		t2=p2.next
		p2.next=t1
		p1=t1
		p2=t2

