# implemented with help from https://codereview.stackexchange.com/questions/114435/python-linked-list?newreg=91a4427ce18048c7a67bbbc101f1ac89

# each node has prev and next

class Node:
    '''Node with data, prev_node, and next_node'''

    def __init__(self, data, prev_node=None, next_node=None):
        '''Initialize the Node'''

        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def __str__(self):
        return self.data


class DoublyLinkedList:
    '''Linked List where each node has prev and next'''

    def __init__(self):
        '''Initialize linked list'''

        self.head = None

    def prepend(self, data):
        '''Replace head with new node'''

        self.head = Node(data, None, self.head)

    def append(self, data):
        '''Add new node to end'''

        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            iter_node = self.head
            while iter_node.next_node:
                iter_node = iter_node.next_node
            new_node.prev_node = iter_node
            iter_node.next_node = new_node

    def insert(self, position, data):
        '''Replace node at position with new node'''

        if ((not self.head) or (position == 0)):
            self.prepend(data)
        else:
            c = 0
            prev_node = self.head
            while prev_node.next_node:
                prev_node = prev_node.next_node
                c += 1
                if c == (position - 1):
                    break
            if prev_node.next_node == None:
                raise KeyError(position)
            new_node = Node(data, prev_node, prev_node.next_node)
            prev_node.next_node = new_node
                

    def delete(self, position):
        '''Remove node at position'''

        if not self.head:
            raise KeyError(position)

        if (position == 0):
            if not self.head.next_node:
                self.head = None
            else:
                self.head = self.head.next_node
                self.head.prev_node = None
        else:
            c = 0
            prev_node = self.head
            while prev_node.next_node:
                prev_node = prev_node.next_node
                c += 1
                if c == (position - 1):
                    break
            if prev_node.next_node == None:
                raise KeyError(position)
            prev_node.next_node = prev_node.next_node.next_node
            prev_node.next_node.prev_node = prev_node

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


double = DoublyLinkedList()
double.prepend('1st prepended')
double.print()
print('printed 1\n')

double.prepend('2nd prepended')
double.print()
print('printed 2\n')

double.append('appended')
double.print()
print('printed 3\n')

double.insert(2, 'inserted at position 2')
double.print()
print('printed 4\n')

double.delete(0)
double.print()
print('printed 5\n')

double.delete(0)
double.delete(0)
double.delete(0)

double.print()