'''
利用列表复现栈的基本操作：初始化，压栈，弹栈，返回栈长，返回栈顶元素，判断栈是否为空
'''


class Stack:
    def __init__(self):
        self.data = []

    def push(self, ele):
        self.data.append(ele)

    def isempty(self):
        return self.data==[]

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            self.data.pop()

    def len(self):
        return len(self.data)

    def gettopele(self):
        if self.isempty():
            print("Stack is empty")
        else:
            return self.data[-1]

if __name__=="__main__":
    '''
    初始化
    '''
    tmp_stack = Stack()
    '''
    操作
    '''
    tmp_stack.push(1)
    tmp_stack.push(2)
    tmp_stack.push(100)
    print("栈长: %s"%tmp_stack.len())
    print("返回栈顶元素: %s"%tmp_stack.gettopele())
    print("栈是否为空: %s"%tmp_stack.isempty())
    tmp_stack.pop()
    tmp_stack.pop()
    tmp_stack.pop()
    print("栈是否为空: %s" % tmp_stack.isempty())
    print("返回栈顶元素: %s" % tmp_stack.gettopele())
    print("栈长: %s" % tmp_stack.len())

    print("END")