'''
队列的实现，以及其基本操作。
使用列表实现
'''

class Queue:
    def __init__(self):
        self.data = []
        self.end_index = None

    def is_empty(self):
        if self.end_index == None:
            return True
        else:
            return False

    def get_head(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.data[0]

    def get_tail(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.data[self.end_index]

    def len(self):
        return len(self.data)

    def enqueue(self,
                item):
        self.data.append(item)
        if self.end_index == None:
            self.end_index = 0
        else:
            self.end_index += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            self.data = self.data[1:]
            if self.len() == 0:
                self.end_index = None
            else:
                self.end_index = self.len() - 1

if __name__ == "__main__":

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print("长度为：%s" % queue.len())
    print("队列头元素为：%s" % queue.get_head())
    print("队列尾元素为：%s" % queue.get_tail())
    print("长度为：%s" % queue.len())

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print("长度为：%s" % queue.len())
    print("队列头元素为：%s" % queue.get_head())
    print("队列尾元素为：%s" % queue.get_tail())
    print("长度为：%s" % queue.len())

    print("END")