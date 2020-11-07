"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""
import collections

class Node:
    def __init__(self, val: int, next=None, prev=None):
        self._val = val
        self._next = next
        self._prev = prev

    def __str__(self):
        return '<{}>'.format(self._val)

class MyLinkedList:
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
        cursor = self._head
        while cursor is not None:
            cursor = cursor._next
            self._size += 1
        return self._size

    def addTwoNumbers(self, l1, l2):
        big = l1 if len(l1) >= len(l2) else l2
        small = l1 if len(l1) < len(l2) else l2
        bigc = big._tail
        smallc = small._tail
        carry = 0
        result = collections.deque()
        while bigc is not None:
            if smallc is not None:
                val = bigc._val + smallc._val + carry
                smallc = smallc._prev
            else:
                val = bigc._val + carry
            carry = int(val/10)
            if carry > 0:
                result.appendleft(val % 10)
            else:
                result.appendleft(val)
            bigc = bigc._prev
        return result

def main():
    l1 = MyLinkedList()
    n1 = Node(2)
    n2 = Node(4)
    n3 = Node(3)
    l1._head = n1
    n1._next = n2
    n2._prev = n1
    n2._next = n3
    n3._prev = n2
    n3._next = None
    l1._tail = n3
    l2 = MyLinkedList()
    m1 = Node(5)
    m2 = Node(6)
    m3 = Node(4)
    m4 = Node(7)
    l2._head = m1
    m1._next = m2
    m2._prev = m1
    m2._next = m3
    m3._prev = m2
    m3._next = m4
    m4._prev = m3
    m4._next = None
    l2._tail = m4
    obj = MyLinkedList()
    print(obj.addTwoNumbers(l1, l2))

if __name__=='__main__':
    main()
