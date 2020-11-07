class MyCircularQueue:

    """ nested non-public Node class """
    class _Node:
        def __init__(self, element:int, next=None):
            self._element = element
            self._next = next

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self._tail = None
        self._size = 0
        self._capacity = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            new = self._Node(value, None)
            if self.isEmpty():
                new._next = new
            elif self._size <= self._capacity:
                new._next = self._tail._next   # pointer to the head of the queue
                self._tail._next = new
            self._tail = new
            self._size += 1
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            old_head = self._tail._next
            new_head = old_head._next
            self._tail._next = new_head
            self._size -= 1
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self._tail._next._element


    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self._tail._element


    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self._size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self._size == self._capacity


if __name__ == "__main__":
    # Your MyCircularQueue object will be instantiated and called as such:
    circularQueue = MyCircularQueue(3)
    assert circularQueue.enQueue(1) == True
    assert circularQueue.enQueue(2) == True
    assert circularQueue.enQueue(3) == True
    assert circularQueue.enQueue(4) == False
    assert circularQueue.Rear() == 3
    assert circularQueue.isFull() == True
    assert circularQueue.deQueue() == True
    assert circularQueue.enQueue(4) == True
    assert circularQueue.Rear() == 4