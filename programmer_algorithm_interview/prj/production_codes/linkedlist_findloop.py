
class LinkedList:

    class Node:
        def __init__(self,
                     data,
                     next
                     ):
            self.data = data
            self.next = next

        def __del__(self):
            print('结点被删除... 内容: %s'%self.data)

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        cur = head
        i = 1
        while i <= head.data:
            tmp = LinkedList.Node(i, None)
            cur.next = tmp
            cur = tmp
            i = i + 1
        self.tail = cur

    def print_whole(self, head):
        '''
        :param head:
        :return:
        '''
        cur = head
        while cur != None:
            print(cur.data)
            cur = cur.next

    def isloop(self):
        '''
        判断链表中是否存在尾环
        :param head:
        :return:
        '''
        slow = self.head
        fast = self.head
        while 1:
            try: # 防止链表太短的溢出情况
                slow = slow.next
                fast = fast.next.next
            except Exception as e:
                print('Exception Happens: %s'%e)
                return 0
            else:
                if slow == None or fast == None:
                    return 0
                elif slow == fast:
                    return 1
                else:
                    continue

if __name__ == '__main__':
    print('构造链表...')
    head = LinkedList.Node(10, None) # 长度为10的有头链表
    tail = LinkedList.Node(None, None)
    linked_list = LinkedList(head, tail)
    print('tail.data = %s tail.next = %s'%(linked_list.tail.data,
                                           linked_list.tail.next))
    linked_list.tail.next = linked_list.head.next.next # 构造尾环
    # print('打印链表...')
    # linked_list.print_whole(head)
    print('检查链表是否有环...:%s'%(linked_list.isloop()))
    print('END')
