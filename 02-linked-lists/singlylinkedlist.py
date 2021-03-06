# implemented with help from https://codereview.stackexchange.com/questions/114435/python-linked-list?newreg=91a4427ce18048c7a67bbbc101f1ac89

class Node:
    '''Node with data and next_node'''

    def __init__(self, data, next_node=None):
        '''Initialize the Node'''

        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    '''Linked List where each node has next'''

    def __init__(self):
        '''Initialize linked list'''

        self.head = None

    def prepend(self, data):
        '''Replace head with new node'''

        self.head = Node(data, self.head)

    def append(self, data):
        '''Add new node to end'''

        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            iter_node = self.head
            while iter_node.next_node:
                iter_node = iter_node.next_node
            iter_node.next_node = new_node

    def insert(self, position, data):
        '''Replace node at position with new node'''

        if (not self.head) or (position == 0):
            self.prepend(data)
        else:
            c = 0
            prev_node = self.head
            while prev_node.next_node:
                prev_node = prev_node.next_node
                c += 1
                if c == (position - 1):
                    break
            if prev_node.next_node is None:
                raise KeyError(position)
            prev_node.next_node = Node(data, prev_node.next_node)

    def delete(self, position):
        '''Remove node at position'''

        if not self.head:
            raise KeyError(position)

        if position == 0:
            if not self.head.next_node:
                self.head = None
            else:
                self.head = self.head.next_node
        else:
            c = 0
            prev_node = self.head
            if c != (position - 1):
                while prev_node.next_node:
                    prev_node = prev_node.next_node
                    c += 1
                    if c == (position - 1):
                        break
            if prev_node.next_node is None:
                raise KeyError(position)
            prev_node.next_node = prev_node.next_node.next_node

    def print(self):
        '''Print linked list'''

        if not self.head:
            print(None)
        else:
            iter_node = self.head
            print(iter_node)
            while iter_node.next_node:
                iter_node = iter_node.next_node
                print(iter_node)


# single = SinglyLinkedList()
# single.prepend('1st prepended')
# single.print()
# print('printed 1\n')

# single.prepend('2nd prepended')
# single.print()
# print('printed 2\n')

# single.append('appended')
# single.print()
# print('printed 3\n')

# single.insert(2, 'inserted at position 2')
# single.print()
# print('printed 4\n')

# single.delete(0)
# single.print()
# print('printed 5\n')
