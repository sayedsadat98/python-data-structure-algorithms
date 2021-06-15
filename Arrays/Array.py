# Arrays is not so common in Python as we use python list mostly

from array import *

# Creating an Array Time : O(1) Space: O(n)
arr1 = array('i', [1, 2, 3, 4, 5, 6])

print(arr1.tolist())  # [1, 2, 3, 4, 5, 6]

## Operation 1a : Insertion (End) --> O(1)
arr1.insert(6, 7)
print(arr1.tolist())  # [1, 2, 3, 4, 5, 6, 7]

## Operation 1b : Insertion (Start) --> O(n)
arr1.insert(0, 0)
print(arr1.tolist())

## Operation 1c : Insertion (Middle) --> O(n)
arr1.insert(2, 300)  # Insert at arr1[2] NOT arr1[3]
print(arr1.tolist())


# Operation 2 : Traverse() --> O(n)
def traverseArray(arr):
    for items in arr:
        print(items, end=' ')


traverseArray(arr1)


# Operation 3 : Accessing an element --> O(1)

def accessElement(arr, index):
    if index >= len(arr):
        print('Array Index Out Of Bounds! Please enter another index')
    else:
        print(arr[index])


accessElement(arr1, 30)

# Operation 4 : Searching for an element --> O(n)
def searchFor(arr,value):
    if value in arr:
        return 'Found at'

    else:
        return 'Not Found!!'

print(searchFor(arr1,25))

# Operation 4a : Searching for an element's index --> O(n)

def indexOf(arr, value):
    flag = False
    for i in range(len(arr)):

        if arr[i] == value:
            return i
            flag = True
            break

    if not flag:
        return -1
print(indexOf(arr1,4))

# Operation 5 : Deleting an element using built-in remove() --> O(n)
arr1.remove(300)
print(arr1.tolist())

