
import random

class LinkList:

    class Node:
        def __init__(self,
                     data,
                     next
                     ):
            self.data = data
            self.next = next

    def __init__(self, head):
        self.head = head
        cur = head
        i = 1
        while i <= head.data:
            tmp = LinkList.Node(i, None)
            print(tmp.data)
            cur.next = tmp
            cur = tmp
            i = i + 1

    def print_linkedlist(self, head):
        '''
        :param head:
        :return:
        '''
        cur = head
        while cur != None:
            print(cur.data)
            cur = cur.next

    def rotate_right(self, head):
        '''
        向右旋转3个结点
        :param head:
        :return:
        '''
        fast = head.next.next.next # 游标fast先于游标slow三个结点出发
        slow = head.next
        pre = head
        while fast.next != None:
            fast = fast.next
            pre = slow
            slow = slow.next
        # 游标fast到达最后一个结点时
        fast.next = head.next
        head.next = slow
        pre.next = None


if __name__ == '__main__':
    print('构造链表...')
    head = LinkList.Node(10, None)
    linked_list = LinkList(head)
    print('打印链表...')
    linked_list.print_linkedlist(head)
    print('向右旋转链表3个单位...')
    linked_list.rotate_right(head)
    print('打印链表...')
    linked_list.print_linkedlist(head)
    print('END')
