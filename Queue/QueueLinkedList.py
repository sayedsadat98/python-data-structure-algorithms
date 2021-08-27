class Node:

    def __init__(self, value):
        self.next = None
        self.value = value

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next


class Queue:

    def __init__(self):
        self.list = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.list]
        return ' '.join(values)

    def isEmpty(self):
        return self.list.head is None

    def enqueue(self, value):
        newNode = Node(value)

        if self.list.head is None:
            self.list.head = newNode
            self.list.tail = newNode

        else:
            self.list.tail.next = newNode
            newNode.next = None
            self.list.tail = newNode

    def dequeue(self):
        if not self.isEmpty():
            targetNode = self.list.head
            value = targetNode.value
            self.list.head = targetNode.next
            return value
        else:
            return 'QUEUE EMPTY'

    def peek(self):
        if self.list.head is not None:

            return self.list.head.value
        else:
            return 'NOTHING'

    def delete(self):
        self.list.head = None
        self.list.tail = None

queue = Queue()
queue.enqueue(3)
queue.enqueue(2)
print(queue)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue)
