# in the classic problem of the towers of hanoi, you have 3 towers and n disks of different sizes which can slide onto any tower. the puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one). you have the following constraints: (1) only one disk can be moved at a time. (2) a disk is slid off the top of one tower onto the next tower. (3) a disk can only be placed on top of a larger disk. write a program to move the disks from the first tower to the last using stacks.

# implemented with help from https://www.youtube.com/watch?v=rVPuzFYlfYE

stack = __import__('02')

def move(a, b):
    '''Move from top of one stack to top of other stack'''

    b.push(a.pop())

def towers(n, f, t, s): # from, to, spare
    if n == 1:
        move(f, t)
        # print('moving from {} to {}'.format(f, t))
    else:
        towers(n - 1, f, s, t)
        towers(1, f, t, s)
        towers(n - 1, s, t, f)

stack_a = stack.Stack()
stack_b = stack.Stack()
stack_c = stack.Stack()

stack_a.push(3)
stack_a.push(2)
stack_a.push(1)

print('\nbefore:')
stack_a.print()
stack_b.print()
stack_c.print()

towers(3, stack_a, stack_b, stack_c)

print('\nafter:')
stack_a.print()
stack_b.print()
stack_c.print()