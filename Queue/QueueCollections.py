'''
We Will use the Collections Module

'''

from collections import deque

queue = deque(maxlen=5)
print(queue)
queue.append(5)
queue.append(1)
queue.append(2)
queue.append(4)
queue.append(43)
queue.append(121212)
print(queue)
queue.popleft()

print(queue)

