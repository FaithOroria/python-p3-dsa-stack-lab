class Stack:

    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.full():
            raise Exception("Stack is full")
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return self.limit is not None and self.size() >= self.limit

    def search(self, target):
        if target in self.items:
            return self.size() - self.items[::-1].index(target) - 1
        return -1


