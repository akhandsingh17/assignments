
"""
       1
    /     \
   2       3
 /  \    /  \
4    5  6    7
              \
               8
               

"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreeTraversal:
    def __init__(self, root):
        self.root = Node(root)

    def preorder(self, start, traversal):
        if start != None:
            traversal = traversal + (str(start.val) + '-')
            traversal = self.preorder(start.left, traversal )
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        if start != None:
            traversal = self.preorder(start.left, traversal)
            traversal = traversal + (str(start.val) + '-')
            traversal = self.preorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        if start != None:
            traversal = self.preorder(start.left, traversal )
            traversal = self.preorder(start.right, traversal)
            traversal = traversal + (str(start.val) + '-')
        return traversal

    def print_traversal(self, type):
        if type == 'preorder':
            return self.preorder(self.root, '')
        if type == 'inorder':
            return self.inorder(self.root, '')
        if type == 'postorder':
            return self.postorder(self.root, '')

def main():
    tree = BinaryTreeTraversal(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.right.right.right = Node(8)
    print(tree.print_traversal('preorder'))
    print(tree.print_traversal('inorder'))
    print(tree.print_traversal('postorder'))

if __name__=='__main__':
    main()

