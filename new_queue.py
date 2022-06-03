from queue_implementation.queue import Queue
from queue_implementation.queue_out_of_range import QueueOutOfRange


class ChildQueue(Queue):
    number_of_instances = 0
    q_dict = {}

    def __init__(self, queue, name, size):
        super().__init__(queue)
        self.name = name
        self.size = size
        ChildQueue.number_of_instances += 1
        ChildQueue.q_dict[self.name] = {'queue': self.queue, 'size': self.size}

    def insert_value(self, value):
        if len(self.queue) < self.size:
            super().insert_value(value)
            return self.queue
        else:
            raise QueueOutOfRange
            return None

    @classmethod
    def retrieve_instance_data_by_name(cls, name):
        return cls.q_dict[name]

    @classmethod
    def save(cls):
        file = open('queue_instances_data.txt', 'a')
        file.write(str(cls.q_dict))
        file.close()

    @classmethod
    def load(cls):
        file = open('queue_instances_data.txt', 'r')
        data = file.read()
        file.close()
        return data
