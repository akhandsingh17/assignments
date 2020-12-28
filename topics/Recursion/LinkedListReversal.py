# Recursive Python3 program to reverse 
# a linked list 
import math

# Link list node 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def LinkedList():
    head = None

# Function to reverse the linked list 
def reverse(node):
    if (node == None):
        return node

    if (node.next == None):
        return node

    node1 = reverse(node.next)
    node.next.next = node
    node.next = None
    return node1

# Function to print linked list 
def printList():
    temp = head
    while (temp != None) :
        print(temp.data, end = " ")
        temp = temp.next

def push(head_ref, new_data):
    new_node = Node(new_data)
    new_node.data = new_data
    new_node.next = head_ref
    head_ref = new_node
    return head_ref

# Driver Code 
if __name__=='__main__':

    # Start with the empty list
    head = LinkedList()
    head = push(head, 20)
    head = push(head, 4)
    head = push(head, 15)
    head = push(head, 85)

    print("Given linked list")
    printList()

    head = reverse(head)

    print("\nReversed Linked list")
    printList()

