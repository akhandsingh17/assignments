"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

"""

class Node(object):
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return 'Node <{}>'.format(self.key, self.value)

class LinkedList(object):
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _removeElement(self, node):
        previous = node.prev
        next = node.next
        previous.next = next
        next.prev = previous

    def _addElement(self, node):
        last = self.tail.prev
        last.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = last

    def __str__(self):
        traverse = lambda x: [str(x)]+traverse(x.next) if x else []
        return '{ ' + ' -> '.join(traverse(self.head)) + ' }'

class LRUCache(object):
    def __init__(self, capacity):
        self.MAX_SIZE = capacity
        self.lookup = {}  # key=query ; value=Node
        self.linkedlist = LinkedList()

    def get(self, key):
        """
        get the stored results from the cache
        """
        node = self.lookup.get(key)
        if node is None:
            return -1
        node = self.lookup[key]
        self.linkedlist._removeElement(node)
        self.linkedlist._addElement(node)
        return node.value

    def put(self, key, value):
        """
       set the result for given query in the cache
       when updating the entry, we need to add the node to the front and if the size of the cache i.e. LinkedList
       has reached the MAX_SIZE then remove the tail node i.e. oldest entry from the list
       """
        node = self.lookup.get(key)
        if node is not None:
            # query exists in the cache. update the value of the node
            node.val = value
            self.linkedlist._removeElement(node)

        new_node = Node(key, value)
        self.linkedlist._addElement(new_node)
        self.lookup[key] = new_node

        # Key does not exist in cache and we need to add this query
        if len(self.lookup) > self.MAX_SIZE:
            # remove oldest entry from the linked list as well as lookup
            nodeToDelete = self.linkedlist.head.next
            self.lookup.pop(nodeToDelete.key, None)
            self.linkedlist._removeElement(nodeToDelete)

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4








