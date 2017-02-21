class Queue:
    '''Queue'''

    def __init__(self):
        '''Initialize queue'''

        self.items = []

    def enqueue(self, data):
        '''Append data to queue'''
        self.items.insert(0, data)

    def dequeue(self):
        '''Remove last item from queue'''
        return self.items.pop()

    def print(self):
        '''Print queue'''

        print(self.items)

# queue = Queue()
# queue.enqueue('First')
# queue.enqueue('Second')
# queue.enqueue('Third')
# queue.enqueue('Fourth')
# queue.print()

# print('\ndequeueing')
# print(queue.dequeue())
# queue.print()