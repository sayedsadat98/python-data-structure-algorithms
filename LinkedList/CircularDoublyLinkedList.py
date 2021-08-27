class Node:

    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return self.value


class CircularList:

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
            if tempNode == self.head:
                break
        return count

    def createList(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode

    def insertAt(self, position, value):

        if self.head is None:  # If the List is empty, it will create a list
            # self.createList(value)
            # return
            pass

        else:  # If the list is not empty
            newNode = Node(value)
            if position == 0:  # Insert at the beginning
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif position >= self.__len__(self):  # Insert at the end
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

            elif 0 < position < self.__len__(self):  # Insert in the middle
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


if __name__ == '__main__':
    List = CircularList()
    print([node.value for node in List])
    #

    List.insertAt(1, 2)
    # List.insertAt(1, 2)
    # List.insertAt(2, 3)
    # List.insertAt(3, 4)
    print([node.value for node in List])
