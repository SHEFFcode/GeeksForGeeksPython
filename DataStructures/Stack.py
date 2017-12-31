class Stack:
    def __init__(self):
        self.items = []

    def __iter__(self):
        length = len(self.items)
        i = 0
        while i < length:
            yield self.items[length - 1 - i]
            i += 1
        raise StopIteration

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()