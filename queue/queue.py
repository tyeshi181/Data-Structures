class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)
        self.size += 1

    def dequeue(self):
        return self.storage.pop(0)
        self.size -= 1

    def len(self):
        return len(self.storage)

    def __str__(self):
        return f'{self.storage}'


line = Queue()
line.enqueue("dog")
line.enqueue("cat")
print(line.size)
print(line)
