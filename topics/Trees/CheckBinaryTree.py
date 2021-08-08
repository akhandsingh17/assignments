"""
# Check if a given tree is a binary Search tree in recursive and iterative both.

"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root):
        self.root = TreeNode(root)
        self.traversal = []

    def inorder_traverse(self, start, traversal):
        if start:
            self.traversal = self.inorder_traverse(start.left, traversal)
            self.traversal.append(int(start.val))
            self.traversal = self.inorder_traverse(start.right, traversal)
        return self.traversal

    def print_tree(self, type):
        if type == 'inorder':
            return self.inorder_traverse(self.root, self.traversal)

    def isBinaryTree(self):
        return all(self.traversal[i] <= self.traversal[i+1] for i in range(len(self.traversal)-1))

def main():
    tree = Tree(10)
    tree.root.left = TreeNode(5)
    tree.root.right = TreeNode(40)
    tree.root.left.left = TreeNode(1)
    tree.root.left.right = TreeNode(7)
    tree.root.right.right = TreeNode(50)
    assert tree.isBinaryTree() == True


if __name__ == '__main__':
    main()
