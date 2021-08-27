class Node:

    def __init__(self, val=None):
        self.next = None
        self.value = val


class List:

    def __init__(self):
        self.head = None

    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next


class StackList:

    def __init__(self):
        self.list = List()

    def __str__(self):
        values = [str(x.value) for x in self.list]
        return ' '.join(values)

    def isEmpty(self):
        return self.list.head is None

    def push(self, value):
        newNode = Node(value)
        if self.list.head is None:
            newNode.next = None
            self.list.head = newNode
        else:
            newNode.next = self.list.head
            self.list.head = newNode

    def pop(self):
        if self.list.head is None:
            return 'Stack is empty'
        else:

            value = self.list.head.value
            self.list.head = self.list.head.next
            return value

    def peek(self):
        if self.list.head is not None:

            return self.list.head.value
        else:
            return 'Stack is empty'

    def delete(self):
        self.list.head = None


stack = StackList()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)

print(stack.peek())
print(stack.pop())
print(stack.peek())
# print(stack.pop())
# print(stack.pop())

# print(stack.isEmpty())
