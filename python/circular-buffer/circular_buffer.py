from collections import deque


class BufferFullException(Exception):
    def __init__(self, message):
        self.message = message


class BufferEmptyException(Exception):
    def __init__(self, message):
        self.message = message


class CircularBuffer(object):
    def __init__(self, capacity):
        self.ring = deque()
        self.capacity = capacity

    def read(self):
        if len(self.ring) == 0:
            raise BufferEmptyException("Empty")
        else:
            return self.ring.popleft()

    def write(self, data):
        if len(self.ring) == self.capacity:
            raise BufferFullException("Full")
        self.ring.append(data)

    def overwrite(self, data):
        if len(self.ring) == self.capacity:
            self.ring.popleft()
        self.write(data)

    def clear(self):
        self.ring = deque()
