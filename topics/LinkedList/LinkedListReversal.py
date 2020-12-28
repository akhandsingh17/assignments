"""
Given pointer to the head node of a linked list, the task is to reverse the linked list.
We need to reverse the list by changing the links between nodes.
"""

# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)

# Node class


class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return '<{}>'.format(self.data)

class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def __str__(self):
        traverse = lambda x: [str(x)]+traverse(x.next) if x else []
        return '{ ' + ' -> '.join(traverse(self.head)) + ' }'


    def reversal(self):
        prev = None
        curr = self.head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

if __name__ == "__main__":
    l = LinkedList()
    Node1 = Node(1)
    Node2 = Node(2)
    Node3 = Node(3)
    Node4 = Node(4)
    Node5 = Node(5)
    l.head = Node1
    Node1.next = Node2
    Node2.next = Node3
    Node3.next = Node4
    Node4.next = Node5
    print(l)
    l.reversal()
    print(l)
