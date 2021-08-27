from LinkedList.LinkedListClass.LinkedList import *

'''
    Question: Return kth element from the last of the linked list
'''


def targetElement(n,list):
    targetNode = list.tail
    # print('Tails value is ', targetNode.value)
    count = 1

    while count < n:
        targetNode = targetNode.prev
        # print('Loops', targetNode.value)

        count += 1

    return targetNode.value


list = LinkedList()
list.generate_values(15, 1, 9)
print(list)

print(targetElement(2, list))
