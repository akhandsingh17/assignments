"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right
to left for the next level and alternate between).
For example:
Given binary tree [3,9,20,null,null,15,7],

  3
 / \
9   20
    / \
   15  7


[
    [3],
    [20,9],
    [15,7]
]
"""

from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        dict = defaultdict(list)
        self.preorder(root, 1, dict)

        levels = []
        for key, value in dict.items():
            if key % 2 == 0:
                levels.append(sorted(value, reverse=True))
            else:
                levels.append(value)

        return levels

    def preorder(self, root, level, dict):
        if root is None:
            return

        dict[level].append(root.val)
        self.preorder(root.left, level+1, dict)
        self.preorder(root.right, level+1, dict)


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = None
    root.left.right = None
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.zigzagLevelOrder(root))