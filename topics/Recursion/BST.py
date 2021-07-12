"""
Given the root node of a binary search tree (BST) and a value.
You need to find the node in the BST that the node's value equals the given value.
Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2

Return
      2
     / \
    1   3
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

     def __str__(self):
         return '<{}>'.format(self.val)

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        if root is None:
            return []

        if root.val == val:
            return root
        else:
            if root.val > val:
                return self.searchBST(root.left, val)
            else:
                return self.searchBST(root.right, val)


if __name__=='__main__':
    s = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)
    print(s.searchBST(root, 2))

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)
    print(s.searchBST(root, 5))