'''
data structure set() as hashset
set_.add()
set_.remove()
'''

import random

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head
        cur = head
        i = 1
        while i <= head.data:
            tmp = Node(random.randint(1, 4), None)
            print(tmp.data)
            cur.next = tmp
            cur = tmp
            i = i + 1

    def print_linkedlist(self):
        '''
        :param head:
        :return:
        '''
        cur = head
        print('Original LinkedList: ')
        while cur != None:
            print(cur.data)
            cur = cur.next

    def remove_duplicate(self):
        '''

        :return:
        '''
        print('LinkedList Duplicate...')
        set_tmp = set()
        cur = head.next
        pre = head
        while cur != None:
            if cur.data in set_tmp:
                pre.next = cur.next
                cur = cur.next
            else:
                set_tmp.add(cur.data)
                pre = cur
                cur = cur.next

if __name__ == '__main__':
    # 初始化链表
    head = Node(8, None)
    linked_list = LinkedList(head)
    # 打印原链表
    linked_list.print_linkedlist()
    # 去除重复项
    linked_list.remove_duplicate()
    # 打印去重后的链表
    linked_list.print_linkedlist()
    print('END')