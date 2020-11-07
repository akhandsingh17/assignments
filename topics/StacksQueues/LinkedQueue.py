""" FIFO implementation using a singly linked list """

class LinkedQueue:
    """ nested non-public _Node class """
    class _Node:
        def __init__(self, element: int, next: "_Node" = None):
            self._element = element
            self._next = next

        def __repr__(self):
            return "Node <{}>".format(self._element)

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def first(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        else:
            return self._head._element

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        else:
            answer = self.head._element
            self._head = self._head._next
            self._size -= 1
            if self.isEmpty():
                self._tail = None
            return answer

    def enqueue(self, e):
        new = self._Node(e)
        if self.isEmpty():
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1


if __name__ == "__main__":
    Myqueue  = LinkedQueue()
    Myqueue.enqueue(12)
    Myqueue.enqueue(15)
    print(Myqueue.first())