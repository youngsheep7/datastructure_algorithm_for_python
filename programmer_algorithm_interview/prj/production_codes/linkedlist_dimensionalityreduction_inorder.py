
'''
扁平化链表
1 2 3 <== 主链表
1 2 3
1 2 3
1   3
    3
'''


class Node:
    '''
    只带一个指针的结点
    '''
    def __init__(self,
                 data,
                 next
                 ):
        self.data = data
        self.next = next

    def __del__(self):
        pass

class Node2Nexts(Node):
    '''
    带两个指针的结点
    '''
    def __init__(self,
                 data,
                 next_1,
                 next_2):
        self.data = data
        self.next_1 = next_1
        self.next_2 = next_2

class LinkedList:

    def __init__(self, tp_data):
        self.head = Node(len(tp_data), None)
        self.data = tp_data

    def init(self):
        '''
        构造链表
        '''
        cur = self.head
        for item in self.data:
            tmp = Node(item, None)
            cur.next = tmp
            cur = tmp

    def print_whole(self):
        ''' 从头结点开始，打印整个链表
        '''
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next

'''
无头链表
'''

if __name__ == '__main__':
    a = Node(1, None)
    b = Node2Nexts(2, None, None)

    print('构造链表...')
    print('打印链表...')
    print('END')
