# implemented with help from https://github.com/calebmadrigal/algorithms-in-python/blob/master/hashtable.py

class HashTable:
    '''Hash table which uses strings as keys'''

    def __init__(self, capacity=1000):
        '''Initialize the HashTable'''

        self.table = []
        for i in range(0, capacity):
            self.table.append([])

    def set(self, key, obj):
        '''Update existing key with value
        If no such key, create new key'''

        found = False

        for data in self.table: # found existing key, update the value
            if data and (data[0] == key):
                found = True
                data[1] = obj
                break

        if not found: # add a new key
            for data in self.table:
                if not data: # data is empty
                    data.append(key)
                    data.append(obj)
                    break

    def get(self, key):
        '''Tries to return object at key
        If key not found, raises KeyError'''

        for data in self.table:
            if data and (data[0] == key):
                return data[1]

        raise KeyError(key)

    def remove(self, key):
        '''Tries to remove data at key
        If key not found, raises KeyError'''

        for data in self.table:
            if data and (data[0] == key):
                self.table.remove(data)
                return

        raise KeyError(key)

ht = HashTable(10)

ht.set('Hello', 'bark')
print(ht.get('Hello'))

print(ht.get('cat')) # KeyError

ht.remove('Hello')
print(ht.get('Hello')) # KeyError
