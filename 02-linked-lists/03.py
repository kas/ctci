# implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node

# implemented with help from https://stackoverflow.com/questions/69209/deleting-a-middle-node-from-a-single-linked-list-when-pointer-to-the-previous-no

from singlylinkedlist import SinglyLinkedList

def delete_node(node):
    node.data = node.next_node.data
    next_node = node.next_node.next_node
    del node.next_node
    node.next_node = next_node

singly = SinglyLinkedList()
singly.append('a')
singly.append(56)
singly.append('b')
singly.append('c')
singly.append('d')
singly.append('a')
singly.append('a')
singly.print()

print('\ndeleting node...\n')

delete_node(singly.head.next_node.next_node) # node is 'b'
singly.print()