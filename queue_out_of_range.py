class QueueOutOfRange(Exception):

    def __init__(self):
        self.message = 'Queue size is out of range'
        super().__init__(self.message)
