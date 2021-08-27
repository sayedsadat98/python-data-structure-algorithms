class Stack:

    def __init__(self,
                 sizeLimit=1000):  # sizeLimit is a default (large) value ; if a size is passed it will take that value
        self.size = sizeLimit
        self.list = []

    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        return ' '.join(values)

    def isEmpty(self):
        return len(self.list) == 0

    def isFull(self):
        return len(self.list) == self.size

    def push(self, value):
        if not self.isFull():
            self.list.append(value)
        else:
            print('STACK OVERFLOW')

    def pop(self):
        if self.isEmpty():
            return 'ERROR!! Stack is empty'
        else:
            temp = self.list[-1]
            del self.list[-1]
            return 'Popped element is ' + str(temp)

    def peek(self):
        return 'The last element is ' + str(self.list[-1])

    def deleteStack(self):
        self.list = None


customStack = Stack()  # with Size Limit
customStack.push(3)
customStack.push(4)
customStack.push(5)
customStack.push(6)
customStack.push(7)
customStack.push(8)
customStack.push(77)
print(customStack.pop())
# print(customStack)
print(customStack.peek())
# print('==============')
# print(customStack.pop())
# print(customStack.peek())
# print('==============')
# customStack.deleteStack()
print(customStack)
