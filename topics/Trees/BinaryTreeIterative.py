
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):

        result = []
        # Base cases
        if root is None:
            return


        # Node stack to store the root, right and left sub-trees
        nodestack = []
        nodestack.append(root)

        while len(nodestack) > 0:
            node = nodestack.pop()
            result.append(node.val)

            if node.right is not None:
                nodestack.append(node.right)

            if node.left is not None:
                nodestack.append(node.left)


        return result



    def inorderTraversal(self, root):

        # base cases
        if root is None:
            return

        nodeStack = []
        result = []
        curr = root

        while (len(nodeStack) != 0 or curr):
            if curr:
                nodeStack.append(curr)
                curr = curr.left
            else:
                curr = nodeStack.pop()
                result.append(curr.val)
                curr = curr.right

        return result


    def postorderTraversal(self, root):

        # Base case

        if root is None:
            return

        nodeStack1 = []
        nodeStack2 = []

        result = []
        nodeStack1.append(root)

        while nodeStack1:
            node = nodeStack1.pop()
            nodeStack2.append(node)

            if node.left:
                nodeStack1.append(node.left)
            if node.right:
                nodeStack1.append(node.right)


        while nodeStack2:
            node = nodeStack2.pop()
            result.append(node.val)

        return result