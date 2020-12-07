"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right
to left for the next level and alternate between).
For example:
Given binary tree [3,9,20,null,null,15,7],

3
/ \
    9  20
/ \
    15   7


[
    [3],
    [20,9],
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
    def zigzagLevelOrder(self, root: TreeNode):

        if root is None:
            return

        levels = []
        level = 0
        q = deque([root], )

        while q:
            level_length = len(q)
            levels.append([])
            for i in range(level_length):

                node = q.popleft()
                if level % 2 == 0:
                    levels[level].append(node.val)
                else:
                    levels[level].appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return levels

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = None
    root.right = TreeNode(3)
    root.right.left = None
    root.right.right = TreeNode(5)
    print(s.zigzagLevelOrder(root))