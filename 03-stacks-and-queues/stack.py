class Node:
    '''Node with data and next_node'''

    def __init__(self, data, next_node=None):
        '''Initialize the Node'''

        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)

class Stack:
    '''Stack'''

    def __init__(self):
        '''Initialize stack'''

        self.top = None

    def pop(self):
        '''Pop value off top of stack'''
        self.top = self.top.next_node

        return self.top

    def push(self, data):
        '''Push value to top of stack'''

        t = self.top
        self.top = Node(data)
        self.top.next_node = t

    def peek(self):
        '''Return top value'''
        if not self.top:
            return None
        return self.top.data

    def print(self):
        '''Print stack'''

        if not self.top:
            print(None)
        else:
            itr_nd = self.top
            print(itr_nd)
            while itr_nd.next_node:
                itr_nd = itr_nd.next_node
                print(itr_nd)

# stack = Stack()
# stack.push('bottom')
# stack.push('middle')
# stack.push('top')
# stack.print()

# print('\npopping!')
# stack.pop()
# stack.print()