# write code to remove duplicates from an unsorted linked list without using a temporary buffer

# implemented with help from https://codereview.stackexchange.com/questions/74845/removing-duplicates-without-using-a-temporary-buffer

from doublylinkedlist import DoublyLinkedList

def find_and_remove_duplicates(doubly):
    iter_node = doubly.head
    while iter_node.next_node:
        runner_node = iter_node.next_node
        while runner_node:
            if runner_node.data == iter_node.data:
                # remove runner_node
                print('removing {}'.format(iter_node.data))

                runner_node.prev_node.next_node = runner_node.next_node
                if runner_node.prev_node.next_node != None:
                    runner_node.prev_node.next_node.prev_node = runner_node.prev_node

            if runner_node.next_node:
                runner_node = runner_node.next_node
            else:
                break
        iter_node = iter_node.next_node

doubly = DoublyLinkedList()
doubly.append('a')
doubly.append(56)
doubly.append('b')
doubly.append('c')
doubly.append('d')
doubly.append('a') # duplicate
doubly.append('a') # duplicate
doubly.append('b') # duplicate
print('no duplicates removed:')
doubly.print()

find_and_remove_duplicates(doubly)
print('\nduplicates removed:')
doubly.print()
