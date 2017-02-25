# imagine a (literal) stack of plates. if the stack gets too high, it might topple. therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).

class SetOfStacks:
    '''SetOfStacks'''

    def __init__(self, limit=3):
        '''Initialize setofstacks'''

        self.stacks = [[]]
        self.limit = limit

    def pop(self):
        '''Pop value off top of setofstacks'''

        if not self.stacks[0]:
            raise IndexError('pop from empty setofstacks')

        data = self.stacks[0][0]
        del self.stacks[0][0]

        for i, stack in enumerate(self.stacks):
            if (len(stack) < self.limit) and ((len(self.stacks) - 1) >= (i + 1)):
                stack.append(self.stacks[i + 1][len(self.stacks[i + 1]) - 1])
                del self.stacks[i + 1][len(self.stacks[i + 1]) - 1]

                if self.stacks[i + 1] == []:
                    del self.stacks[i + 1]

        return data

    def pop_at(self, s_i):
        '''Pop value off top of specified stack in setofstacks'''

        # check if popping off stack[99999] will crash the program

        if (len(self.stacks) - 1) < s_i:
            raise IndexError('pop from empty stack in setofstacks')

        data = self.stacks[s_i][0]
        del self.stacks[s_i][0]

        for i, stack in enumerate(self.stacks):
            if i < s_i:
                continue

            if (len(stack) < self.limit) and ((len(self.stacks) - 1) >= (i + 1)):
                stack.append(self.stacks[i + 1][len(self.stacks[i + 1]) - 1])
                del self.stacks[i + 1][len(self.stacks[i + 1]) - 1]

                if self.stacks[i + 1] == []:
                    del self.stacks[i + 1]

        return data

    def push(self, data):
        '''Push value to top of setofstacks'''

        self.stacks[0].insert(0, data)

        for i, stack in enumerate(self.stacks):
            if len(stack) > self.limit:
                if (len(self.stacks) - 1) < (i + 1):
                    self.stacks.append([])

                self.stacks[i + 1].insert(0, stack[len(stack) - 1])
                del stack[len(stack) - 1]

    def print(self):
        '''Print setofstacks'''

        for stack in self.stacks:
            print(stack)

# set_of_stacks = SetOfStacks()
# set_of_stacks.push('First pushed')
# set_of_stacks.push('Second pushed')
# set_of_stacks.push('Third pushed')
# set_of_stacks.push('Fourth pushed')
# set_of_stacks.push('Fifth pushed')
# set_of_stacks.push('Sixth pushed')
# set_of_stacks.push('Seventh pushed')
# set_of_stacks.push('Eighth pushed')
# set_of_stacks.push('Ninth pushed')
# set_of_stacks.push('Tenth pushed')
# set_of_stacks.print()

# print('\npopping:')
# set_of_stacks.pop()
# set_of_stacks.pop()
# set_of_stacks.print()

# print('\npopping from stack at index 1:')
# set_of_stacks.pop_at(1)
# set_of_stacks.print()