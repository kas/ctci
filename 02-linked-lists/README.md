# 2 linked lists

## know how to implement a linked list from scratch

## understand difference between singly linked list and doubly linked list
* doubly linked list has prev and next
* singly has only next

## deleting a node
* update (prev) and next
* ! check for the null pointer

## runner technique
* iterate through linked list with 2 pointers
  * one pointer ahead of the other
  * fast node could be fixed distance or could hop n for every 1 the slow node hops

## many linked list problems rely on recursion
* recursive algorithms take at least o(n) space
  * n is depth of recursive call