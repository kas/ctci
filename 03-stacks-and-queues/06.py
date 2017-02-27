# sort a stack in ascending order (biggest items on top). may use one additional stack to hold items. stacks have push, pop, peek, and isEmpty

class Stack:
    '''Stack'''

    def __init__(self):
        '''Initialize stack'''

        self.items = []

    def pop(self):
        '''Pop value off top of stack'''

        return self.items.pop()

    def push(self, data):
        '''Push value to top of stack'''

        self.items.append(data)

    def peek(self):
        '''Return top value in stack'''

        if not self.items:
            return None

        return self.items[len(self.items) - 1]

    def is_empty(self):
        '''Return whether stack is empty'''

        if not self.items:
            return True

        return False

    def print(self):
        '''Print stack'''

        print(self.items)

def sort_ascending(s):
    n = Stack() # new stack

    while not s.is_empty():
        if  n.is_empty() or (s.peek() > n.peek()):
            n.push(s.pop())
        else:
            i = s.pop() # item
            c = 0 # counter

            while n.peek() and n.peek() >= i:
                s.push(n.pop())
                c += 1

            n.push(i)

            while c > 0:
                n.push(s.pop())
                c -= 1

    return n

s = Stack()
s.push(3)
s.push(1)
s.push(2)
s.push(5)
s.push(1)
s.push(0)
s.push(0)
s.push(1)
s.push(-1)

print('\nbefore:')
s.print()

print('\nafter:')
sort_ascending(s).print()