import random

" All important methods of Doubly Linked List can be found here"


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

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

    def __str__(self):
        values = [str(x.value) for x in self]
        return '<->'.join(values)

    def __len__(self):
        count = 0
        currentNode = self.head
        while currentNode:
            count += 1
            currentNode = currentNode.next

        return count

    def add(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            newNode.next = None
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def delete(self, index):
        '''
        index : Starts from 0
        '''

        if self.head is None:
            print('Invalid')
            return
        elif index == 0:
            targetNode = self.head
            targetNode.next.prev = None
            self.head = targetNode.next

        elif index >= (len(self)) - 1:
            targetNode = self.tail
            targetNode.prev.next = None
            self.tail = targetNode.prev

        else:
            pointer = 0

            currentNode = self.head
            while pointer < index:
                currentNode = currentNode.next
                pointer += 1
            nextNode = currentNode.next
            prevNode = currentNode.prev

            prevNode.next = nextNode
            nextNode.prev = prevNode

    def generate_values(self, n, minVal, maxVal):
        for i in range(n):
            num = random.randint(minVal, maxVal)
            self.add(num)
            # print('Value is', num)

    def reverse(self):
        currentNode = self.tail
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.prev


# list = LinkedList()
# list.add(2)
# list.add(5)
# list.add(7)
# list.add(6)
# list.add(8)
# list.add(8)
# # list.generate_values(15, 1, 9)
# print(list)
# # print(len(list))
#
# list.delete(5)
# print(list)

# list.reverse()
# print(list)

# list.delete(2)
# print((list))
# list.delete(2)
# print((list))
