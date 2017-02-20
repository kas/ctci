# implement a function to check if a linked list is a palindrome

from doublylinkedlist import DoublyLinkedList

def palindrome(doubly):
    palindrome = False

    s = ''
    itr_nd = doubly.head
    while itr_nd:
        s += str(itr_nd.data)
        itr_nd = itr_nd.next_node

    if s[::-1] == s:
        palindrome = True

    return palindrome

doubly = DoublyLinkedList()
doubly.append('k')
doubly.append('a')
doubly.append('y')
doubly.append('a')
doubly.append('k')
doubly.print()

print(palindrome(doubly))

doubly = DoublyLinkedList()
doubly.append('c')
doubly.append('a')
doubly.append('n')
doubly.append('o')
doubly.append('e')
doubly.print()

print(palindrome(doubly))