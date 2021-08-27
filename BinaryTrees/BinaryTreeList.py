# Create a binary tree given a Python list
# input: [3,5,2,1,4,6,7,8,9,10,11,12,13,14]

"""
          3
       /     \
     5         2
    /\         /\
   1  4       6   7
  /\  /\     /\   /\
 8 9 10 11 12 13 14
"""
import queue as Q


class Node:

    def __init__(self, value=None):
        self.value = value
        self.left = self.right = None


class BinaryTree:

    def isEmpty(self):
        return self.root

    def insertElements(self, arr, root, i, n):
        if i < n:
            newNode = Node(arr[i])
            root = newNode

            root.left = self.insertElements(arr, root.left, 2 * i + 1, n)
            root.right = self.insertElements(arr, root.right, 2 * i + 2, n)

        return root

    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.left)
            print(root.value, end=' ')
            self.inOrder(root.right)

    def levelOrderTraverse(self, root):
        que = Q.Queue()
        que.put(root)
        elements = []
        while not que.empty():
            root = que.get()
            elements.append(root.value)
            if root.left is not None:
                que.put(root.left)

            if root.right is not None:
                que.put(root.right)
        return elements

    def search(self, root, value):
        elements_extracted = self.levelOrderTraverse(root)
        if value in elements_extracted:
            print('Found')
        else:
            print('not found')

    # def insert(self, root, value):
    #     if root is None:
    #         newNode = Node(value)
    #         root = newNode
    #     else:
    #         que = Q.Queue()
    #         que.put(root.value)
    #
    #         while not que.empty():
    #             root= que.get()
    #
    #             if root.left is None:




arr = [3, 5, 2, 1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
n = len(arr)
i = 0
root = None
tree = BinaryTree()
root = tree.insertElements(arr, root, i, n)
# tree.inOrder(root)
# tree.levelOrderTraverse(root)
tree.search(root, 7)