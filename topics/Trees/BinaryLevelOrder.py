"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode):

        levels = []

        if root is None:
            return levels

        q = deque([root, ])
        level = 0

        while q:
            levels.append([])
            level_length = len(q)

            for i in range(level_length):
                node = q.popleft()
                levels[level].append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return levels



if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = None
    root.left.right = None
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.levelOrder(root))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(s.levelOrder(root))