class BufferFullException(Exception):
    def __init__(self):
        Exception.__init__(self,r".+")


class BufferEmptyException(Exception):
    def __init__(self):
        Exception.__init__(self,r".+")


class CircularBuffer(object):
    data = []
    capacity = 0
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity

    def read(self):
        if len(self.data) <= 0:
            raise BufferEmptyException
        date = self.data[0]
        self.data.pop(0)
        return date

    def write(self, data):
        if len(self.data) >= self.capacity:
            raise BufferFullException
        self.data.append(data)

    def overwrite(self, data):
        if len(self.data) == self.capacity:
            self.data.pop(0)
        self.data.append(data)

    def clear(self):
        self.data = []
