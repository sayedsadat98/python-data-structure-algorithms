class Node:

    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def length(self):
        """
        Returns the length of the Linked List

        :return: count (int) : Length of the list
        """
        tempNode = self.head
        count = 0

        while tempNode is not None:
            count += 1
            tempNode = tempNode.next

        return count

    def insertAt(self, position, value):
        """
        Used to insert values into linked list
        :param position: Index (i.e. take 0 into consideration) where you want to insert the new value
        :param value: The data/value that you want to insert
        :return: String if there user enters a negative index
        """
        newNode = Node(value)

        if self.head is None:  # If the List was empty from the beginning
            self.head = newNode
            self.tail = newNode

        else:
            if position == 0:  # Insert at Start
                newNode.next = self.head
                self.head = newNode

            elif position >= self.length():  # Insert at end
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            elif 0 < position < self.length():  # Insert in the middle
                index = 0
                tempNode = self.head
                while index < position - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                tempNode.next = newNode
            else:  # To handle negative indices
                return 'You have entered an invalid index'

    def deleteNode(self, position):
        """
        Deletes a particular node of the linked list
        :param position: Value of the index location that you want to delete
        :return: String if there is an error
        """
        if self.head is None:
            print('List is empty nothing to delete')

        else:
            if self.length() == 1:  # If there is only 1 node in the list
                self.head = None
                self.tail = None
                return

            if position == 0:  # Delete the first node (current Head)
                self.head = self.head.next
            elif position >= self.length():
                targetNode = self.head
                index = 0
                while index < self.length() - 2:
                    targetNode = targetNode.next
                    index += 1
                targetNode.next = None
                self.tail = targetNode

            elif 0 < position < self.length():
                tempNode = self.head
                index = 0
                nodeBefore = None
                while index <= position:
                    if index == position - 1:
                        nodeBefore = tempNode
                    tempNode = tempNode.next
                    index += 1
                nodeBefore.next = tempNode
            else:
                print('Illegal index')

    def deleteList(self):
        """
        Deletes the entire List
        :return: String if there is an error
        """
        if self.length() == 0:
            print('List has no node')

        else:
            self.head = None
            self.tail = None

    def traverseList(self):
        """
        Visits each node element of the list and print the node's value
        :return: String of node values
        """
        if self.head is None:
            print('List Is Empty')

        else:
            pointer = self.head
            print('[[', end=' ')
            while pointer is not None:
                print(pointer.value, end=' ')
                pointer = pointer.next
            print(']]')

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


# Example of a driver code ; You can use your own driver code
if __name__ == '__main__':
    SingleList = SinglyLinkedList()
    SingleList.insertAt(1, 1)
    SingleList.insertAt(1, 2)
    SingleList.insertAt(2, 3)
    SingleList.insertAt(3, 4)
    SingleList.insertAt(4, 5)
    SingleList.insertAt(0, 0)
    SingleList.insertAt(3, 23)
    SingleList.insertAt(13, 6)

    # print([nodes.value for nodes in SingleList])
    print(SingleList.traverseList())
    # print(SingleList.search(90))

    SingleList.deleteNode(2)

    print(SingleList.traverseList())
    SingleList.insertAt(13, 9999)

    print(SingleList.traverseList())
    #
    print(SingleList.length())
