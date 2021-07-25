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
    def __init__(self, data):
        self.data = data
        self.next = None


    def __str__(self):
        return 'Node <{}>'.format(self.data)


class Solution:
    def __init__(self):
        self.head = None

    def __str__(self):
        traverse = lambda x: [str(x)] + traverse(x.next) if x else []
        return '{ ' + ' -> '.join(traverse(self.head)) + ' }'

    def deleteDuplicates(self):
        curr = self.head
        prev = None
        while curr:
            next = curr.next
            prev = curr
            if prev.data == next.data:
                prev.next = next.next
            curr = curr.next

if __name__ == "__main__":
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(2)
    n4 = ListNode(3)
    n5 = ListNode(3)
    s.head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    print(s)
    s.deleteDuplicates()
    print(s)