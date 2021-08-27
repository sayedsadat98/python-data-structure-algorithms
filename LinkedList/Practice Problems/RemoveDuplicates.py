'''

    Question: Given a List, Remove the duplicates

'''

from LinkedList.LinkedListClass.LinkedList import LinkedList as List


def remove_duplicates(inputList):
    currentNode = inputList.head
    visited = set([currentNode.value])
    inputList = inputList.head

    while currentNode.next:
        value = currentNode.value
        if value in visited:
            currentNode.next = currentNode.next.next

        else:
            visited.add(currentNode.next.value)
        return inputList


# def remove_duplicates(input_list):
#     if input_list.head is None:
#         return
#     else:
#         visited = set([input_list.head.value])
#         count = 1
#         currentNode = input_list.head
#         value = currentNode.value
#         while currentNode.next:
#
#             if value not in visited:
#                 visited.append(value)
#             else:
#                 List().delete(count)
#
#             currentNode = currentNode.next
#             count += 1

# list = List()
# list.generate_values(5, 1, 9)
# print(list)
#
# remove_duplicates(list)
# print(list)
