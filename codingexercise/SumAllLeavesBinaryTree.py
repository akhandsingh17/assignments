# Sum of All leaves in a Binary Tree

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


class BinaryTree(object):
    def __init__(self,root):
        self.root=Node(root)

    def preorder(self,start,traversal):
        if start!=None:
            traversal=traversal+ (str(start.value)+ '-')
            traversal=self.preorder(start.left,traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self,start,traversal):
        if start!=None:
            traversal = self.preorder(start.left, traversal)
            traversal=traversal+ (str(start.value)+ '-')
            traversal = self.preorder(start.right, traversal)
        return traversal

    def postorder(self,start,traversal):
        if start!=None:
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
            traversal = traversal + (str(start.value) + '-')
        return traversal

    def print_tree(self,traversal_type):
        if traversal_type=='preorder':
            return self.preorder(self.root,'')
        elif traversal_type=='inorder':
            return self.inorder(self.root,'')
        elif traversal_type=='postorder':
            return self.postorder(self.root,'')

    def CaculateSum(self,start,tmp):

        if start is None:
            return
        if start.left is  None and start.right is None:
            tmp.append(start.value)
            return
        self.CaculateSum(start.left,tmp)
        self.CaculateSum(start.right,tmp)

    def SumAllLeavesBinaryTree(self):

        tmp=[]
        self.CaculateSum(self.root,tmp)
        sum=0
        for l in tmp:
            sum=sum+l
        return sum

    def SumAllLeavesBinaryTreeWithoutRecurrsion(self):

        start=self.root
        node_lst=[]
        num_lst=[]
        node_lst.append(start)
        while len(node_lst)>0:
            tmp=[]
            while len(node_lst)>0:
                n=node_lst[-1]
                node_lst.pop()
                if n.left is None and n.right is None:
                    num_lst.append(n.value)

                if n.left!=None:
                    tmp.append(n.left)
                if n.right!=None:
                    tmp.append(n.right)

            node_lst=tmp
        sum=0
        for l in num_lst:
            sum=sum+l
        return sum

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    tree.root.right.left=Node(6)
    tree.root.right.right=Node(7)
    tree.root.left.left.left=Node(8)
    tree.root.left.left.right = Node(9)
    tree.root.left.right.left = Node(10)
    tree.root.left.right.right = Node(11)
    tree.root.right.left.left = Node(12)
    tree.root.right.left.right = Node(13)
    tree.root.right.right.left = Node(14)
    tree.root.right.right.right = Node(15)
    print(tree.print_tree('preorder'))
    print(tree.print_tree('inorder'))
    print(tree.print_tree('postorder'))
    print(tree.SumAllLeavesBinaryTree())
    print(tree.SumAllLeavesBinaryTreeWithoutRecurrsion())

if __name__=='__main__':
    main()