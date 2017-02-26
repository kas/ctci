# implement myqueue class which implements a queue using 2 stacks

# implemented with help from https://stackoverflow.com/questions/69192/how-to-implement-a-queue-using-two-stacks

stack = __import__('02')

class Queue:
    '''Queue'''

    def __init__(self):
        '''Initialize queue'''

        self.in_s = stack.Stack()
        self.out_s = stack.Stack()

    def enqueue(self, data):
        '''Append data to queue'''

        self.in_s.push(data)

    def dequeue(self):
        '''Remove last item from queue'''

        if not self.out_s.items:
            while self.in_s.items:
                self.out_s.push(self.in_s.pop())

        return self.out_s.pop()

    def print(self):
        '''Print queue'''

        print(self.in_s)
        print(self.out_s)

# queue = Queue()
# queue.enqueue('First')
# queue.enqueue('Second')
# queue.enqueue('Third')
# queue.enqueue('Fourth')
# queue.print()

# print('\ndequeueing')
# print(queue.dequeue())
# queue.print()