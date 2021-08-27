import queue as Q


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inOrderTraverse(root):
    if root is None:
        return
    else:
        preOrderTraverse(root.left)
        print(root.value)
        preOrderTraverse(root.right)


def preOrderTraverse(root):
    if root is None:
        return
    else:
        print(root.value)
        preOrderTraverse(root.left)
        preOrderTraverse(root.right)


def postOrderTraverse(root):
    if root is None:
        return
    else:
        preOrderTraverse(root.left)
        preOrderTraverse(root.right)
        print(root.value)


def levelOrderTraverse(root):

    que = Q.Queue()
    que.put(root)

    while not que.empty():
        root = que.get()
        print(root.value)
        if root.left is not None:
            que.put(root.left)

        if root.right is not None:
            que.put(root.right)




newBT = TreeNode('Drinks')
leftChild = TreeNode('Cola')
rightChild = TreeNode('Sprit')

newBT.left = leftChild
newBT.right = rightChild

levelOrderTraverse(newBT)

# postOrderTraverse(newBT)
