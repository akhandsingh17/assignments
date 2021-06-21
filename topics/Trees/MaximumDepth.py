"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest
leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2

"""

from collections import deque
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        depth = 1
        levels = []
        # Base condition
        if root is None:
            return 0

        q = deque()
        q.append(root)
        q.append(None)

        while len(q) > 1:
            node = q.popleft()
            if node is None:
                q.append(None)
                depth += 1
            else:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return depth

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = None
    root.left.right = None
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert s.maxDepth(root) == 3

    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    assert s.maxDepth(root) == 2

    root = None
    assert s.maxDepth(root) == 0

    root = TreeNode(0)
    assert s.maxDepth(root) == 1
