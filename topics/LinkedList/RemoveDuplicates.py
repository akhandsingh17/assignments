"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

"""

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return 'Node <{}>'.format(self.val)

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = head
        head = head.next
        while head:
            if prev.val == head.val:
                prev.next = head.next
                head.next = None
            head = head.next
        return head

if __name__ == "__main__":
    l1 = Solution()
    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(2)
    n4 = ListNode(3)
    n5 = ListNode(3)
    l1.head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    print(l1)
    s = Solution()
    (s.deleteDuplicates(l1))
    print(l1)