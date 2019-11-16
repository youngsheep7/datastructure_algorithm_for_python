"""
二叉树中序遍历构造和中序遍历打印
"""


class Node:
    def __init__(self,
                 data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BinaryTree:
    def __init__(self,
                 array):
        self.data = array
        self.root = self.__construct(self.data)

    def __construct(self,
                    data):
        root = Node(None)
        if len(data) == 1:
            root.data = data[0]
            return root
        else:
            mid_index = int(len(data)/2)
            root.data = data[mid_index]
            if mid_index-1 >= 0:
                root.lchild = self.__construct(data[:mid_index])
            if mid_index+1 <= len(data)-1:
                root.rchild = self.__construct(data[mid_index+1:])
            return root

    @staticmethod
    def inorder_print(root: Node):
        if root is None:
            return
        else:
            BinaryTree.inorder_print(root.lchild)
            print(root.data)
            BinaryTree.inorder_print(root.rchild)


if __name__ == "__main__":
    array = [item for item in range(1,11)]
    binarytree = BinaryTree(array)
    BinaryTree.inorder_print(binarytree.root)
    print("END")
