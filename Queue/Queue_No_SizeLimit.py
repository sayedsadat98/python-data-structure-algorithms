# Python List with no capacity/limit


class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(item) for item in self.items]
        return ' '.join(values)

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)

    def deque(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return 'Queue is Empty'

    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            return 'Queue is Empty'

    def delete(self):
        self.items = None


que = Queue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
print(que.deque())
print(que)
