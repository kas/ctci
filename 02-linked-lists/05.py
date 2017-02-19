# you have two numbers represented by a linked list where each node contains a single digit. digits are stored in reverse order, such that the 1s digit is at the head of the list. write a function that adds the 2 numbers and returns the sum as a linked list

from doublylinkedlist import DoublyLinkedList

def add(doubly_one, doubly_two):
    one = ''
    itr_nd = doubly_one.head
    while itr_nd:
        one += str(itr_nd.data)
        itr_nd = itr_nd.next_node

    two = ''
    itr_nd = doubly_two.head
    while itr_nd:
        two += str(itr_nd.data)
        itr_nd = itr_nd.next_node

    s = int(one[::-1]) + int(two[::-1])
    s = str(s)

    s = s[::-1]
    doubly_s = DoublyLinkedList()
    for c in s:
        doubly_s.append(int(c))

    return doubly_s

print('\ndoubly_one...\n')

doubly_one = DoublyLinkedList()
doubly_one.append(3)
doubly_one.append(2)
doubly_one.append(1)
doubly_one.print()

print('\ndoubly_two...\n')

doubly_two = DoublyLinkedList()
doubly_two.append(6)
doubly_two.append(5)
doubly_two.append(2)
doubly_two.print()

print('\ndoubly_sum...\n')

doubly_sum = add(doubly_one, doubly_two)
doubly_sum.print() # expect 379