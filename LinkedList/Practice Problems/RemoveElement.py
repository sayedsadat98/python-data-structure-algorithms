'''
    Question: Remove an element from the linked list
'''

from LinkedList.LinkedListClass.LinkedList import *


def removeElements(target, list):
    currentNode = list.head
    index = 0
    while currentNode:
        if target == currentNode.value:
            list.delete(index)
        index += 1
        currentNode = currentNode.next

    return list


list = LinkedList()
list.generate_values(10, 1, 6)
print(list)
print(removeElements(4, list))

# Try with 6->4->2->1->4->4->5->2->3->4