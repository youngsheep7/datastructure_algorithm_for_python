import random

class LinkedListNode:
	def __init__(self, data, next):
		self.data = data
		self.next = next

def __init_linkedlist(hashead, i_length, isdatarandom):
	'''
	:param hashead:
	:param i_length:
	:param isdatarandom:
	:return:
	'''

	if hashead == True:
		head = LinkedListNode(i_length, None)
		cur = head
		i = 1
		while i <= i_length:
			tmp = LinkedListNode(random.randint(1,20), None)
			print(tmp.data)
			cur.next = tmp
			cur = tmp
			i = i + 1
		return head

def __print_linkedlist(head):
	'''
	:param head:
	:return:
	'''
	cur = head
	while cur != None:
		print(cur.data)
		cur = cur.next

def __reverse_linkedlist(head):
	'''
	:param head:
	:return:
	'''
	if head == None or head.next == None:
		return head
	cur = head.next.next
	head.next.next = None
	while cur!= None:
		next = cur.next
		cur.next = head.next
		head.next = cur
		cur = next
	return head

if __name__ == '__main__':
	# 构造链表
	head = __init_linkedlist(True, 10, True)
	print('#################################')
	# 打印原链表
	__print_linkedlist(head)
	print('#################################')
	# 链表逆序
	head = __reverse_linkedlist(head)
	# 打印逆序后的链表
	__print_linkedlist(head)
	print('END')