# write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x

from doublylinkedlist import DoublyLinkedList

def partition(x):
    found = False
    itr_nd = doubly.head
    c = 0
    while itr_nd:
        if not found:
            if itr_nd.data > x:
                # remove and append
                d = itr_nd.data
                doubly.delete(c)
                doubly.append(d)
            elif itr_nd.data == x:
                found = True
        elif found:
            if itr_nd.data < x:
                # remove and prepend
                d = itr_nd.data
                doubly.delete(c)
                doubly.prepend(d)
        itr_nd = itr_nd.next_node
        c += 1

doubly = DoublyLinkedList()
doubly.append(8)
doubly.append(56)
doubly.append(9)
doubly.append(55)
doubly.append(57)
doubly.print()

print('\npartitioning...\n')

partition(56)
doubly.print()