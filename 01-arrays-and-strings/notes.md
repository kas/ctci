# 1 arrays and strings

## hash tables
* maps keys to values for highly efficient lookup
* when inserting obj+key, hash funct maps keys to integer
  * int is index in array
* hash value of all possible keys must be unique or we could overwrite data
  * instead of making large array and storing objects at index hash(key), make array smaller and store obj in linked list at index hash(key) % array length
    * to get obj of key, search linked list for key
  * or make hash table with binary search tree
    * we can keep tree balanced, so o(logn)
    * can use less space
  * know how to implement in python

## arraylist (dynamically resizing array)
* resizes itself as needed, always providing o(1) access
* typically when array is full it doubles in size
  * doubling takes o(n) time but happens rarely
  * amortized time still o(1)

## string buffer
* creates array of all strings, copying them back to a string only when necessary