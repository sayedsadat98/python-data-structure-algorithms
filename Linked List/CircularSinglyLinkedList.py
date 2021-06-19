class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def length(self):
        """
        Returns the length of the Linked List

        :return: count (int) : Length of the list
        """
        currentNode = self.head
        count = 0
        while currentNode.next != self.head:
            count += 1
            currentNode = currentNode.next
        return count

    def createNode(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.next = self.head

    def insertAt(self, position, value):
        """
        Used to insert values into linked list
        :param position: Index (i.e. take 0 into consideration) where you want to insert the new value
        :param value: The data/value that you want to insert
        :return: String if there user enters a negative index
        """
        newNode = Node(value)

        if self.head is None:  # If the List is empty, it will create a list
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
            return

        elif position == 0:  # Insert at the beginning
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode

        elif position >= self.length():  # Insert at the end
            self.tail.next = newNode
            newNode.next = self.head
            self.tail = newNode

        elif 0 < position < self.length():
            tempNode = self.head
            index = 0
            while index < position - 1:
                tempNode = tempNode.next
                index += 1
            newNode.next = tempNode.next
            tempNode.next = newNode

        else:  # To handle negative indices
            return 'You have entered an invalid index'

    def deleteNode(self, position):
        if self.head is None:  # If the list is empty
            return 'List is empty'
        if self.head == self.tail:  # Case 1: Only 1 element in List
            self.head = None
            self.tail = None
            return

        else:  # Case 2: There are more than 1 elements in List
            if position == 0:  # Delete the first node
                self.head = self.head.next
                self.tail.next = self.head

            elif position >= self.length():  # Delete the last node
                tempNode = self.head
                index = 0
                while index < self.length() - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = self.head
                self.tail = tempNode

            elif 0 < position < self.length():
                tempNode = self.head
                index = 0
                prevNode = None
                while index < position:
                    if index == position - 1:
                        prevNode = tempNode
                    tempNode = tempNode.next
                    index += 1
                prevNode.next = tempNode.next
            else:
                return 'Invalid index entered'

    def listTraversal(self):
        """
        Visits each node element of the list and print the node's value
        :return: String of node values
        """
        if self.head is None:
            print('List is Empty')
        else:
            tempNode = self.head
            print('[[ ', end='')
            while tempNode:
                print(tempNode.value, end=' ')
                tempNode = tempNode.next
                if tempNode == self.head:
                    break

            print(']]')

    def deleteList(self):
        """
        Deletes the entire List
        :return: String if there is an error
        """
        if self.length() == 0:
            print('List has no node')

        else:
            self.head = None
            self.tail.next = None
            self.tail = None

    def search(self, data):
        """
        Search the list for a specific value
        :param data: (int) The value that you are trying to search
        :return: String specifying if the value is found or not
        """
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
    List = CircularLinkedList()
    List.insertAt(1, 1)
    List.insertAt(1, 2)
    List.insertAt(2, 3)
    List.insertAt(3, 4)
    List.insertAt(4, 5)
    List.insertAt(0, 0)
    List.insertAt(20, 6)
    List.insertAt(3, 23)
    List.insertAt(11, 7)

    ans = [node.value for node in List]
    print(ans)
    List.listTraversal()
    print(List.length())
    print(List.search(23))
    List.deleteNode(0)
    List.listTraversal()
    print(List.length())
