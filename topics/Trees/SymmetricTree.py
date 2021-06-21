"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Follow up: Solve it both recursively and iteratively.

"""

import queue

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:


        if root is None:
            return True

        q = queue.SimpleQueue()
        q.put(root)
        q.put(root)

        while q.qsize() > 0 :
            T1 = q.get()
            T2 = q.get()


            if T1 is None and T2 is None:
                continue

            if T1 is None or T2 is None:
                return False

            if T1.val != T2.val:
                return False

            q.put(T1.left)
            q.put(T2.right)
            q.put(T1.right)
            q.put(T2.left)

        return True


if __name__ == "__main__":

    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(s.isSymmetric(root))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = None
    root.left.right = TreeNode(3)
    root.right.left = None
    root.right.right = TreeNode(3)
    print(s.isSymmetric(root))


