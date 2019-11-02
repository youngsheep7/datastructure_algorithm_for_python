
'''
merge 2 orderd linked list into one linked list
'''

class LinkedList:

    class Node:
        def __init__(self,
                     data,
                     next
                     ):
            self.data = data
            self.next = next

        def __del__(self):
            print('结点被删除... 数据域值为 %s'%self.data)

    def __init__(self, lt_data):
        self.head = LinkedList.Node(len(lt_data), None)
        self.lt_data = lt_data

    def init(self):
        '''
        构造链表
        :return:
        '''
        cur = self.head
        for item in self.lt_data:
            tmp = LinkedList.Node(item, None)
            cur.next = tmp
            cur = tmp

    def print_whole(self):
        ''' 从头打印整个链表
        :param head:
        :return:
        '''
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next

def merge2orderedlinkedlist(linkedlist_1, linkedlist_2):
    '''
    将两个有序的链表合并为一个有序的链表
    :param linkedlist_1:
    :param linkedlist_2:
    :return: merged linkedlist
    '''
    if linkedlist_1.head.data == 0 and linkedlist_2.head.data > 0:
        return linkedlist_2
    elif linkedlist_2.head.data == 0 and linkedlist_1.head.data > 0:
        return linkedlist_1
    elif linkedlist_1.head.data == 0 and linkedlist_2.head.data == 0:
        return None
    else:
        cur_1 = linkedlist_1.head.next
        cur_2 = linkedlist_2.head.next
        if cur_1.data < cur_2.data:
            reslinkedlist = linkedlist_1
            cur_main = reslinkedlist.head
        else:
            reslinkedlist = linkedlist_2
            cur_main = reslinkedlist.head
        while cur_1 != None and cur_2!= None:
            if cur_1.data < cur_2.data:
                cur_main.next = cur_1
                cur_main = cur_1
                cur_1 = cur_1.next
            else:
                cur_main.next = cur_2
                cur_main = cur_2
                cur_2 = cur_2.next
        # 如果有一个链表提前遍历结束
        if cur_1 == None: # 链表1提前结束
            cur_main.next = cur_2
        else: # 链表2提前结束
            cur_main.next = cur_1
        return reslinkedlist

if __name__ == '__main__':
    print('构造链表...')
    linkedlist_1 = LinkedList([1,4,5])
    linkedlist_1.init()
    linkedlist_2 = LinkedList([2,3,8,11,14])
    linkedlist_2.init()
    reslinkedlist = merge2orderedlinkedlist(linkedlist_1, linkedlist_2)
    print('打印链表...')
    reslinkedlist.print_whole()
    print('END')
