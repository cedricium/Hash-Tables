class LinkedPair:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        """
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        """
        return hash(key)

    def _hash_djb2(self, key):
        """
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        """
        pass

    def _hash_mod(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        """
        hash = self._hash_mod(key)

        # first check if index of array is empty
        # if it is, create a new LinkedPair with current key:value
        if self.storage[hash] == None:
            self.storage[hash] = LinkedPair(key, value)
        # otherwise, connect new key:value LinkedPair to the end of linked list
        else:
            current_node = self.storage[hash]
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = LinkedPair(key, value)

    def remove(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        """
        pass

    def retrieve(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        """
        hash = self._hash_mod(key)
        linked_pair = self.storage[hash]

        # if no key found, return None
        if linked_pair == None:
            return None
        # if first item in linked list matches given key, return its value
        elif linked_pair.key == key:
            return linked_pair.value
        # otherwise, iterate through linked list and find matching key & return its value
        else:
            current_node = linked_pair
            while current_node.key != key:
                current_node = current_node.next
            return current_node.value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        """
        pass


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

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
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
