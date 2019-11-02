"""
LCR(Least Recently Used)代码实现，基于deque实现
1、内容不存在，则插入deque最左侧
2、内容存在，则将其移至最左侧
"""
from collections import deque


class LCR:
    def __init__(self,
                 size):
        self.size = size
        self.queue = deque()
        self.queue_hashset = set()

    def _en_lcr(self,
               item):
        if len(self.queue) == self.size:
            self._de_lcr()
        self.queue.appendleft(item)
        self.queue_hashset.add(item)

    def _de_lcr(self):
        self.queue_hashset.remove(self.queue[-1])
        self.queue.pop()

    def _update_lcr(self,
                    item):
        self.queue.remove(item)
        self.queue.appendleft(item)

    def print(self):
        for item in self.queue:
            print("%s "%item, end="")
        print("\n")

    def access_item(self,
                    item):
        if item in self.queue_hashset:
            self._update_lcr(item)
        else:
            self._en_lcr(item)


if __name__ == "__main__":
    lcr = LCR(4)
    lcr.access_item(1)
    lcr.print()
    lcr.access_item(2)
    lcr.print()
    lcr.access_item(5)
    lcr.print()
    lcr.access_item(1)
    lcr.print()
    lcr.access_item(6)
    lcr.print()
    lcr.access_item(7)
    lcr.print()
    lcr.access_item(5)
    lcr.print()

    print("END")