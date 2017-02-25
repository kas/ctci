# how would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element? push, pop, and min should all operate in o(1) time

# implemented with help from https://stackoverflow.com/questions/685060/design-a-stack-such-that-getminimum-should-be-o1

class Stack:
    '''Stack'''

    def __init__(self):
        '''Initialize stack'''

        self.items = []
        self.min_items = []

    def pop(self):
        '''Pop value off top of stack'''

        self.min_items.pop()

        return self.items.pop()

    def push(self, data):
        '''Push value to top of stack'''

        self.items.append(data)

        if not self.min_items or (data < self.min_items[len(self.min_items) - 1]):
            self.min_items.append(data)
        else:
            self.min_items.append(self.min_items[len(self.min_items) - 1])

    def minimum(self):
        '''Return minimum value in stack'''

        if not self.items:
            return None

        return self.min_items[len(self.min_items) - 1]

    def print(self):
        '''Print stack'''

        print(self.items)

# stack = Stack()
# stack.push(3)
# stack.push(2)
# stack.push(1)
# stack.print()

# print('\nminimum:')
# print(stack.minimum())

# print('\npopping:')
# stack.pop()
# stack.print()

# print('\nminimum:')
# print(stack.minimum())