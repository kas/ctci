# write code to remove duplicates from an unsorted linked list

from doublylinkedlist import DoublyLinkedList
from collections import defaultdict

def find_duplicates(doubly):
    '''https://stackoverflow.com/questions/11236006/identify-duplicate-values-in-a-list-in-python'''

    l = []

    iter_node = doubly.head
    l.append(iter_node.data)
    while iter_node.next_node: # add all nodes to list to find linked list indices of each node data
        l.append(iter_node.next_node.data)
        iter_node = iter_node.next_node

    D = defaultdict(list)
    for i, item in enumerate(l):
        D[item].append(i)
    D = {k:v for k,v in D.items() if len(v)>1} # iterate over keys and values in D and append to new D if there are duplicate values
    return D

doubly = DoublyLinkedList()
doubly.append('a')
doubly.append(56)
doubly.append('b')
doubly.append('c')
doubly.append('d')
doubly.append('a')
doubly.append('a')

duplicates = find_duplicates(doubly)
while duplicates:
    print('Deleting node at index {}'.format(duplicates[list(duplicates.keys())[0]][-1]))
    doubly.delete(duplicates[list(duplicates.keys())[0]][-1])
    duplicates = find_duplicates(doubly)

doubly.print()
