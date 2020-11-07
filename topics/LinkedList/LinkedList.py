class MyLinkedList:

    class _Node:
        def __init__(self, val: int, next=None):
            self._val = val
            self._next = next

        def __str__(self):
            return 'Node <{}>'.format(self._val)

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._head = None
        self._tail = None
        self._size = 0

    def __str__(self):
        traverse = lambda x: [str(x)]+traverse(x._next) if x else []
        return '{ ' + ' -> '.join(traverse(self._head)) + ' }'

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def get_node(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self._size:
            return -1
        curr = self._head
        for j in range(index):
            curr = curr._next
        return curr

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self._size:
            return -1
        curr = self._head
        for j in range(index):
            curr = curr._next
        return curr._val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        new = self._Node(val)
        new._next = self._head
        self._head = new
        self._size += 1


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new = self._Node(val)
        if self._tail:
            self._tail._next = new
        else:
            self._head._next = new
        self._tail = new
        self._size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list,
        the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index > self._size:
            return
        else:
            if index == 0:
                self.addAtHead(val)
            if index == len(self):
                self.addAtTail(val)

            prev = self.get_node(index-1)
            new = self._Node(val)
            new._next = prev._next
            prev._next = new
            self._size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self._head = self._head._next
            self._size -= 1
        old = self.get_node(index)
        prev = self.get_node(index-1)
        prev._next = old._next
        old = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

"""
MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
"""

if __name__ == "__main__":
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)
    linkedList.addAtTail(3)
    linkedList.addAtIndex(1,2)
    assert (linkedList.get(1)) == 2
    linkedList.deleteAtIndex(1)
    assert (linkedList.get(1)) == 3
    print(linkedList)


