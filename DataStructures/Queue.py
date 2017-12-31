class Queue:
    def __init__(self, capacity):
        self.front, self.rear, self.size, self.capacity = 0, (capacity - 1), 0, capacity
        self.container = [0] * capacity

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            return
        self.rear = (self.rear + 1) % self.capacity
        self.container[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return
        item = self.container[self.front]
        self.container[self.front] = 0
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def get_front(self):
        return -1 if self.is_empty() else self.container[self.front]

    def get_rear(self):
        return -1 if self.is_empty() else self.container[self.rear]
