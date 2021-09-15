"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6


"""
from typing import Optional, List
from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return 'Node <{}>'.format(self.val)

    def __lt__(self, other):
        return self.val < other.val

    def __le__(self, other):
        return self.val <= other.val

    def __eq__(self, other):
        return self.val == other.val

    def __ne__(self, other):
        return self.val != other.val

    def __gt__(self, other):
        return self.val > other.val

    def __ge__(self, other):
        return self.val >= other.val


class QueueNode:
    def __init__(self, listNode):
        self.listNode = listNode

    def __str__(self):
        return '<QNode{}>'.format(self.listNode)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = PriorityQueue()
        head = point = ListNode(0)
        for listNode in lists:
            if listNode:
                pq.put(listNode)

        while pq.qsize() > 0:
            node = pq.get()
            point.next = ListNode(node.val)
            point = point.next
            node = node.next
            if node:
                pq.put(node)
        return head.next

    def print(self, head):
        traverse = lambda x: [str(x)] + traverse(x.next) if x else []
        return '{ ' + ' -> '.join(traverse(head)) + ' }'


if __name__ == '__main__':
    s = Solution()
    n00 = ListNode(1)
    n01 = ListNode(4)
    n02 = ListNode(5)
    n00.next = n01
    n01.next = n02
    n10 = ListNode(1)
    n11 = ListNode(3)
    n12 = ListNode(4)
    n10.next = n11
    n11.next = n12
    n20 = ListNode(2)
    n21 = ListNode(6)
    n20.next = n21
    lists = [n00, n10, n20]
    print(s.print(s.mergeKLists(lists)))
