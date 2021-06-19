class Node:

    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None


class DoublyList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next

    def __len__(self):
        tempNode = self.head
        count = 0

        while tempNode:
            count += 1
            tempNode = tempNode.next
        return count

    def createList(self, value):
        node = Node(value)
        self.head = node
        self.tail = node

    def insertAt(self, position, value):
        if self.head is None:  # If the List is empty, it will create a list
            self.createList(value)
            return
        else:
            newNode = Node(value)
            if position == 0:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode

            elif position >= self.__len__():
                newNode.next = None
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode

            elif 0 < position < self.__len__():
                index = 0
                tempNode = self.head
                while index < position - 1:
                    tempNode = tempNode.next
                    index += 1

                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next.prev = newNode
                tempNode.next = newNode
            else:
                print('Invalid index entered ')

    def deleteNode(self, position):
        if self.head is None:
            print('List is empty')
            return

        if self.__len__() == 1:  # If there is 1 node in list
            self.head = None
            self.tail = None

        else:
            if position == 0:
                newHead = self.head.next
                newHead.prev = None
                self.head = newHead

            elif position >= self.__len__():
                newTail = self.tail.prev
                newTail.next = None
                self.tail = newTail

            elif 0 < position < self.__len__():
                tempNode = self.head
                index = 0
                while index < position - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next.next  # next node : Node next to the deleted node
                nextNode.prev = tempNode
                tempNode.next = nextNode
            else:
                print('Invalid index entered')

    def deleteList(self):
        tempNode = self.head
        while tempNode:
            tempNode.prev = None
            tempNode = tempNode.next
        self.head = None
        self.tail = None

    def traverse(self):
        tempNode = self.head
        while tempNode:
            print(tempNode.value, end=' ')
            tempNode = tempNode.next
        print()

    def reverse(self):
        tempNode = self.tail
        while tempNode:
            print(tempNode.value, end=' ')
            tempNode = tempNode.prev
        print()

    def search(self, data):
        if self.head is None:
            return 'List is empty'
        else:
            tempNode = self.head

            while tempNode:
                if tempNode.value == data:
                    return str(data) + ' found!!'
                tempNode = tempNode.next
            return str(data) + ' Not found'


if __name__ == '__main__':
    List = DoublyList()
    print([node.value for node in List])
    List.insertAt(1, 1)
    List.insertAt(1, 2)
    List.insertAt(2, 3)
    List.insertAt(3, 4)
    List.insertAt(4, 5)
    List.insertAt(5, 6)
    print([node.value for node in List])
    print('Length = ' + str(len(List)))

    List.insertAt(0, 0)
    List.insertAt(List.__len__(), 100)
    print([node.value for node in List])
    print('Length = ' + str(len(List)))
    # List.traverse()
    # List.reverse()
    List.insertAt(2, 12)
    print([node.value for node in List])
    print('Length = ' + str(len(List)))
    List.traverse()
    List.reverse()
    # print(List.search(230))
    print('========================')
    List.traverse()
    List.deleteNode(List.__len__())
    List.traverse()
    List.reverse()
