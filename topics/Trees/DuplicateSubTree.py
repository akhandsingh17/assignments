"""
Check if a Binary Tree contains duplicate subtrees of size 2 or more
Given a Binary Tree, check whether the Binary tree contains a duplicate sub-tree of size 2 or more.
Note : Two same leaf nodes are not considered as subtree size of a leaf node is one.

Input :  Binary Tree
               A
             /    \
           B        C
         /   \       \
        D     E       B
                     /  \
                    D    E
Output : Yes
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

subtrees = {}

class BinaryTree:
    def __init__(self, root: Node):
        self.data = []
        self.marker = '#'
        self.root = Node(root)

    def preorder(self, start, traverse):
        if start:
            traverse = traverse + str(start.val) + '-'
            traverse = self.preorder(start.left, traverse)
            traverse = self.preorder(start.right, traverse)
        return traverse

    def printTree(self):
        print(self.preorder(self.root, ''))

    def serialize(self):
        global subtrees
        def encode(node):
            if node:
                self.data.append(str(node.val))
                encode(node.left)
                encode(node.right)
            else:
                self.data.append(self.marker)

        encode(self.root)

        s = ''.join(self.data)
        if len(s) > 3 and s in subtrees:
            return ""
        subtrees[s] = 1
        return True if "" in s else False


def main():
    tree = BinaryTree('A')
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.right = Node('B')
    tree.root.right.right.left = Node('D')
    tree.root.right.right.right = Node('E')
    assert tree.serialize() == True


if __name__ == '__main__':
    main()
