# implement an algorithm which returns the nodes at the beginning of the loop

# implemented with help from https://stackoverflow.com/questions/10880672/how-can-we-find-the-starting-node-of-a-loop-in-link-list

from doublylinkedlist import DoublyLinkedList

def find_beginning_of_loop(doubly):
    itr_nd_tortoise = doubly.head
    itr_nd_hare = doubly.head

    itr_nd_tortoise = itr_nd_tortoise.next_node
    itr_nd_hare = itr_nd_hare.next_node.next_node

    while itr_nd_tortoise != itr_nd_hare:
        print('first while loop')
        itr_nd_tortoise = itr_nd_tortoise.next_node
        itr_nd_hare = itr_nd_hare.next_node.next_node

    itr_nd_tortoise = doubly.head

    while itr_nd_tortoise != itr_nd_hare:
        print('second while loop')
        itr_nd_tortoise = itr_nd_tortoise.next_node
        itr_nd_hare = itr_nd_hare.next_node

    beginning = itr_nd_tortoise.data
    return beginning

doubly = DoublyLinkedList()
doubly.append('A')
doubly.append('B')
doubly.append('C')
doubly.append('D')
doubly.append('E')
doubly.head.next_node.next_node.next_node.next_node.next_node = doubly.head.next_node.next_node # E.next_node = C
print('doubly is set')

print(find_beginning_of_loop(doubly))