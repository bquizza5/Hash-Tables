# import time
# import hashlib

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        
        hashed_key = self._hash(key)
        index = self._hash_mod(hashed_key)
        if self.retrieve(key) == 'key not found':
            newItem = LinkedPair(key, value)
            if self.storage[index] == None:
                self.storage[index] = newItem
            else:
                node = self.storage[index]
                while node.next != None:
                    node = node.next
                
                node.next = newItem
        else:
            node = self.storage[index]
            while node.key != key:
                if node.next == None:
                    return 'line 73 error. node.next should never == None'
                node = node.next
            node.value = value
            




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''


        if self.retrieve(key) == 'key not found':
            return None

        else:

            hashed_key = self._hash(key)
            index = self._hash_mod(hashed_key)

            if self.storage[index].key == key:
                self.storage[index] = self.storage[index].next
            else:
                prev = self.storage[index]
                current = self.storage[index].next
                while current.key != key:
                    if current == None:
                        return None
                    else:
                        prev = current
                        current = current.next
                prev.next = current.next





    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash(key)
        index = self._hash_mod(hashed_key)

        if not self.storage[index]:
            return 'key not found'
        else:

            node = self.storage[index]
            while node.key != key:

                if node.next == None:
                    return 'key not found'

                node = node.next
            
            if node == None:
                return 'key not found'
            else:
                return node.value



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        old_storage = self.storage
        self.storage = [None] * self.capacity
        for i in old_storage:
            current = i
            while current != None:
                self.insert(current.key, current.value)
                current = current.next





if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    print('***items added***')


    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    ht.remove('line_3')
    ht.remove('line_1')
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))


    print("")


# class DynamicArray:
#     def __init__(self, capacity=8):
#         self.count = 0  # Count is how much is currently used
#         self.capacity = capacity  # How much is currently allocated
#         self.storage = [None] * self.capacity

#     def insert(self, index, value):
#         if self.count == self.capacity:
#             self.resize()
#             return
#         # Shift everything to the right
#         for i in range(self.count, index, -1):
#             self.storage[i] = self.storage[i - 1]
#         # Insert our value
#         self.storage[index] = value
#         self.count += 1

#     def append(self, value):
#         self.insert(self.count, value)

#     def resize(self):
#         self.capacity *= 2
#         new_storage = [None] * self.capacity
#         for i in range(self.count):
#             new_storage[i] = self.storage[i]
#         self.storage = new_storage

#     def replace(self, index, value):
#         self.storage[index] = value

#     def add_to_front(self, value):
#         self.insert(0, value)

#     def slice(self, beginning_index, end_index): # default value
#         # beginning and end
#         # create subarray to store value
#         # copy beginning  to end to subarray
#         # decide how this works.  What happens  to the original array?
#         # leave it alone?  Or cut out what  we're slicing
#         # return subarray