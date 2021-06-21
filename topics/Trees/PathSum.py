"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the
path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


"""

import queue

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

     def __repr__(self):
         return  '<Node-{}>'.format(self.val)

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if root is None:
            return False

        if root.val == sum and root.left is None and root.right is None:
            return True

        return self.hasPathSum(root.left, sum - root.val) or \
               self.hasPathSum(root.right, sum - root.val)

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.right = None
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = None
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)
    root.right.right.left = None
    print(s.hasPathSum(root, 22))