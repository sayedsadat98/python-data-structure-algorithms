# Queue Data Structure implemented using the built in Queue module


import queue as Q

customQueue = Q.Queue(maxsize=5)
print(customQueue.qsize())
print(customQueue.empty())
customQueue.put(1)
# customQueue.put(12)
# customQueue.put(13)
# customQueue.put(14)
# print(customQueue.qsize())
# print(customQueue.get())
# print(customQueue.qsize())
# print(customQueue.empty())
