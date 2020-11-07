from assignments.topics.StacksQueues.EmptyException import EmptyStackException

""" Circular Queue using singly linked list for round robin scheduler  """
class CircularQueue:
    """ nested non-public _Node class """
    class _Node:
        def __init__(self, element: int, next: "_Node" = None):
            self._element = element
            self._next = next

        def __repr__(self):
            return "Node <{}>".format(self._element)

    def __init__(self):
        self._tail = None
        self._size = 0

    def isEmpty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size

    def enqueue(self, e: int) -> None:
        new = self._Node(e, None)
        if self.isEmpty():
            new._next = new
        else:
            new._next = self._tail._next # new node points to head
            self._tail._next = new
        self._tail = new
        self._size += 1

    def dequeue(self) -> int:
        if self.isEmpty():
            raise EmptyStackException
        old_head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            new_head = old_head._next
            self._tail._next = new_head
        self._size -= 1
        return old_head._element

    def first(self) -> int:
        if self.isEmpty():
            raise EmptyStackException
        else:
            return self._tail._next._element

if __name__ == "__main__":
    Myqueue  = CircularQueue()
    Myqueue.enqueue(12)
    Myqueue.enqueue(15)
    print(Myqueue.first())



