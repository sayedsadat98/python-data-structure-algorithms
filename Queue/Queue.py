# Python List with capacity/limit (Efficient Version)


class Queue:

    def __init__(self, maxSize=0):
        self.maxSize = maxSize
        self.top = -1
        self.start = -1
        self.items = maxSize * [None]  # Initialize an empty list with value NONE and size = maxSize

    def __str__(self):
        values = [str(item) for item in self.items]
        return ' '.join(values)

    def __len__(self):
        return len(self.items)

    def isFull(self):
        if self.top + 1 == self.start:
            return True

        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True

        else:
            return False

    def isEmpty(self):
        return self.top == self.start == -1

    def enqueue(self, value):
        if not self.isFull():

            if self.top + 1 == self.maxSize:
                self.top = 0

            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
        else:
            return 'Queue is full'

    def dequeue(self):
        if not self.isEmpty():
            val = self.items[self.start]
            
            return val
        else:
            return 'Queue is Empty'

    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            return 'Queue is Empty'

    def delete(self):
        self.items = None


que = Queue(5)
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
print(que.dequeue())
print(que)
