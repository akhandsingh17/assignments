class DoublyLinkedBase:
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

    def __str__(self):
        traverse = lambda x: [str(x)]+traverse(x._next) if x else []
        return '{ ' + ' -> '.join(traverse(self._head)) + ' }'

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

    def move_to_front(self, node):
        self._insert_between(node._element, self._head, self._head._next)


    def remove_from_tail(self):
        if self.isEmpty():
            raise Exception('Linked list is empty')
        return self._delete_node(self._tail._prev)