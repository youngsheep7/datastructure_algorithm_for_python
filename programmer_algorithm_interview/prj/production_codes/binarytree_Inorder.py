"""
二叉树的中序遍历实现
中序：Left Root Right
"""


class Node:
    def __init__(self,
                 data: int):
        self.data = data
        self.lchild = None
        self.rchild = None


class BinaryTree:
    def __init__(self):
        pass

    @staticmethod
    def inorder_print(
                      root: Node):
        if root is None:
            return
        else:
            BinaryTree.inorder_print(root.lchild)
            print(root.data)
            BinaryTree.inorder_print(root.rchild)


def main():
    node_6 = Node(6)
    node_3 = Node(3)
    node_7 = Node(7)
    node_2 = Node(2)
    node_4 = Node(4)
    node_1 = Node(1)
    node_5 = Node(5)
    node_8 = Node(8)
    node_9 = Node(9)
    node_6.lchild = node_3
    node_6.rchild = node_7
    node_3.lchild = node_2
    node_3.rchild = node_4
    node_2.lchild = node_1
    node_4.rchild = node_5
    node_7.rchild = node_9
    node_9.lchild = node_8
    node_1.lchild = node_1.rchild = \
        node_2.rchild = \
        node_4.lchild = \
        node_5.lchild = node_5.rchild = \
        node_7.lchild = \
        node_9.rchild = \
        node_8.lchild = node_8.rchild = None
    BinaryTree.inorder_print(node_6)


if __name__ == "__main__":
    main()
    print("END")
