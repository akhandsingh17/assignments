
class ArrayQueue:
    """FIFO queue implementaion using python list"""

    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __int__(self):
        """ Create an empty queue """
        self._data =[None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def isEmpty(self):
        """ Return True if queue is empty """
        return self._size == 0

    def __len__(self):
        return self._size

    def first(self):
        """ Return (but not remove) the first element from the queue """
        if self.isEmpty():
            raise Exception("Queue is empty !")
        else:
            return self._data[self._front]

    def dequeue(self):
        """ remove and return the first element from the queue (i.e. FIFO) """
        if self.isEmpty():
            raise Exception("Queue is empty !")
        else:
            if 0 < self._size < len(self._data) // 4:
                self._resize(len(self._data) // 2)
            ans = self._data[self._front]
            self._data[self._front] = None      # help garbage collector to reclaim space
            self._front = (self._front + 1) % len(self._data)
            self._size -= 1
            return ans

    def enqueue(self, e):
        """ Add an element e to the back of queue (i.e. FIFO) """
        if self._size == len(self._data):
            self._resize(2 * len(self._data))   # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self, cap):
        """ Resize the array to a new capacity """
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0
