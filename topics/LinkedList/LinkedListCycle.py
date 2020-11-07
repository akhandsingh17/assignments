
class Solution:
    class Node:
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

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def hasCycle(self, head: Node) -> bool:
        if head is None:
            raise Exception('Linkedlist is empty')
        self._fast_pointer = self._head._next
        self._slow_pointer = self._head
        while self._slow_pointer._next:
            if self._fast_pointer._next is None:
                return False
            self._slow_pointer = self._slow_pointer._next
            self._fast_pointer = self._fast_pointer._next._next
            if self._fast_pointer == self._slow_pointer:
                 return self._slow_pointer
            else:
                continue
        return False

if __name__ == "__main__":
    head = Solution.Node(3)
    link = Solution()
    link._head = head
    p = Solution.Node(2)
    link._head._next = p
    q = Solution.Node(0)
    p._next = q
    s = Solution.Node(-4)
    q._next = s
    s._next = p
    print(link.hasCycle(head))
