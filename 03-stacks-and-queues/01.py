# describe how you could use a single array to implement three stacks

class ThreeStacks:
    '''Three Stacks'''

    def __init__(self):
        '''Initialize three stacks'''

        self.items = []
        self.one_len = 0
        self.two_len = 0

    def pop(self, stack_num):
        '''Pop value off top of stack stack_num'''

        if (stack_num == 1) and (self.one_len > 0):
            i = 0
            self.one_len -= 1
        elif stack_num == 2 and (self.two_len > 0):
            i = self.one_len
            self.two_len -= 1
        elif stack_num == 3:
            i = self.one_len + self.two_len
        else:
            raise IndexError(stack_num)

        item = self.items[i]

        del self.items[i]

        return item

    def push(self, data, stack_num):
        '''Push value to top of stack stack_num'''

        if stack_num == 1:
            i = 0
            self.one_len += 1
        elif stack_num == 2:
            i = self.one_len
            self.two_len += 1
        elif stack_num == 3:
            i = self.one_len + self.two_len
        else:
            raise IndexError(stack_num)

        self.items.insert(i, data)

    def peek(self, stack_num):
        '''Return top value of stack stack_num'''

        if stack_num == 1:
            i = 0
        elif stack_num == 2:
            i = self.one_len
        elif stack_num == 3:
            i = self.one_len + self.two_len
        else:
            raise IndexError(stack_num)

        return self.items[i]

    def print(self):
        '''Print three stacks'''

        print('one_len:')
        for x in range(0, self.one_len):
            print(self.items[x])

        print('\ntwo_len:')
        for x in range(self.one_len, self.one_len + self.two_len):
            print(self.items[x])

        print('\nthree_len:')
        for x in range(self.one_len + self.two_len, len(self.items)):
            print(self.items[x])

# three_stacks = ThreeStacks()
# three_stacks.push('first Push to first stack', 1)
# three_stacks.push('first Push to second stack', 2)
# three_stacks.push('first Push to third stack', 3)
# three_stacks.push('second Push to third stack', 3)

# print('\nprinting:')
# three_stacks.print()

# print('\npeeking:')
# print(three_stacks.peek(3))

# print('\npopping:')
# print(three_stacks.pop(3))

# print('\nprinting:')
# three_stacks.print()