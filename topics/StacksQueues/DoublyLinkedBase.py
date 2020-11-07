class _DoublyLinkedBase:

    class _Node:
        def __init__(self, element, prev=None, next=None):
            self._element = element
            self._prev = prev
            self._next = next

        def __str__(self):
            return 'Node <{}>'.format(self._element)

    def __init__(self):
        self._head = self._Node(None)
        self._tail = self._Node(None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0


    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        new = self._Node(e, predecessor, successor)
        predecessor._next = new
        successor._prev = new
        self._size += 1
        return new

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._element = node._prev = node._next = None
        return element



