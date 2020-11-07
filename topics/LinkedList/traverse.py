# Construct a linked list in Python

class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

def main():
    linklst = LinkedList()
    node1 = Node('Monday')
    node2 = Node('Tuesday')
    node3 = Node('Wednesday')
    linklst.head = node1
    node1.next = node2
    node2.next = node3
    print(linklst.head.value + ' -> ' + linklst.head.next.value)


if __name__== '__main__':
    main()