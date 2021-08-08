"""
Given a binary tree, write a function that returns true if the tree satisfies below property.
For every node, data value must be equal to sum of data values in left and right children. Consider data value as 0 for
NULL children. Below tree is an example

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root: Node):
        self.root = Node(root)

    def children_sum(self, node):
        left_data = 0
        right_data = 0

        if node is None or (node.left is None and node.right is None):
            return 1
        else:
            if node.left:
                left_data = node.left.val
            if node.right:
                right_data = node.right.val

            if (node.val == left_data + right_data) and self.children_sum(node.left) and self.children_sum(node.right):
                return 1
            else:
                return 0

    def isSumProperty(self):
        return self.children_sum(self.root)

def main():
    tree = BinaryTree('10')
    tree.root.left = Node('8')
    tree.root.right = Node('2')
    tree.root.left.left = Node('3')
    tree.root.left.right = Node('5')
    tree.root.right.left = Node('2')
    print(tree.isSumProperty())


if __name__ == '__main__':
    main()
