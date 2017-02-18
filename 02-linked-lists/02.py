# implement an algorithm to find the kth to last element of a singly linked list

from singlylinkedlist import SinglyLinkedList

def find_kth_to_last(singly, k):
    c = 0
    itr_nd = singly.head
    while itr_nd.next_node:
        c += 1
        itr_nd = itr_nd.next_node
    c += 1

    if ((c - k) < 0) or (k <= 0):
        raise IndexError(k)
    else:
        trgt = c - k
        c = 0
        itr_nd = singly.head
        for c in range(0, (trgt)):
            if itr_nd.next_node:
                itr_nd = itr_nd.next_node
        return itr_nd.data

singly = SinglyLinkedList()
singly.append('a')
singly.append(56)
singly.append('b')
singly.append('c')
singly.append('d')
singly.append('a')
singly.append('a')
singly.print()

print('Found it: {}'.format(find_kth_to_last(singly, 7)))
print('Found it: {}'.format(find_kth_to_last(singly, 3)))
# print('Found it: {}'.format(find_kth_to_last(singly, 0)))
# print('Found it: {}'.format(find_kth_to_last(singly, -1)))