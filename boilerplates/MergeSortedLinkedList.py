# Definition for singly-linked list.

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

     def __str__(self):
        return 'Node <{}>'.format(self.val)

class Solution:

    def __int__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        traverse = lambda x: [str(x)] + traverse(x.next) if x else []
        return '{' + '->'.join(traverse(self.head)) + '}'

    def mergeTwoLists(self, l1: ListNode, l2: ListNode, l3: ListNode) -> ListNode:
        cursor1 = l1.head
        cursor2 = l2.head
        prehead = ListNode(None)
        l3.head = prehead
        cursor3 = l3.head

        while cursor1 and cursor2:
            if cursor1.val < cursor2.val:
                cursor3.next = cursor1
                cursor1 = cursor1.next
            else:
                cursor3.next = cursor2
                cursor2 = cursor2.next
            cursor3 = cursor3.next
        return cursor3.next

if __name__ == "__main__":
    l1 = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(4)
    l1.head = n1
    n1.next = n2
    n2.next = n3
    l2 = Solution()
    m1 = ListNode(1)
    m2 = ListNode(3)
    m3 = ListNode(4)
    l2.head = m1
    m1.next = m2
    m2.next = m3
    print(l1, l2)
    s = Solution()
    l3 = Solution()
    print(s.mergeTwoLists(l1, l2, l3))
    print(l3)