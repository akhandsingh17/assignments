"""
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes. Only nodes itself may be changed

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Input: head = [1]
Output: [1]
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '<{}>'.format(self.val)

class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        first = head
        second = head.next

        first.next = self.swapPairs(second.next)
        second.next = first

        return second

    def __str__(self):
        traverse = lambda x: [str(x)]+traverse(x.next) if x else []
        return '{ ' + ' -> '.join(traverse(head)) + ' }'

if __name__ == "__main__":
    head = ListNode(1)
    Node1 = ListNode(2)
    Node2 = ListNode(3)
    Node3 = ListNode(4)
    head.next = Node1
    Node1.next = Node2
    Node2.next = Node3
    s = Solution()
    print(s.swapPairs(head))
