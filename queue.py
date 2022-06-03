class Queue:

    def __init__(self, queue):
        self.queue = queue

    def __str__(self):
        return str(self.queue)

    def insert_value(self, value):
        self.queue.insert(len(self.queue), value)
        return self.queue

    def pop_value(self):
        if len(self.queue):
            popped_value = self.queue.pop(0)
            return popped_value

        else:
            print('Warning: queue is empty')
            return None

    def is_empty(self):
        if not len(self.queue):
            return True
        else:
            return False
