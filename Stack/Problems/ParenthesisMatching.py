# from collections import deque
#
# stack = deque()
#
# var = 'Hello'
# for chars in var:
#     stack.append(chars)
# st = ''
# n=0
# while n < len(var):
#     st += stack.pop()
#     n+=1
#
# print(st)

# s = ["h","e","l","l","o"]
# print(s[::-1])


def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    s[:] = s[::-1]
    return s





