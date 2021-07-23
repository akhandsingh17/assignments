
class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SerializeBT:
    def __init__(self):
        self.marker = '#'

    def serialize(self, root):
        self.vals = []
        def encode(node):
            if node:
                self.vals.append(str(node.val))
                encode(node.left)
                encode(node.right)
            else:
                self.vals.append(self.marker)

        encode(root)
        return ' '.join(self.vals)


    def deserialize(self, data):
        def decode(vals):
            val = next(vals)
            if val == self.marker:
                return None
            node = TreeNode(int(val))
            node.left = decode(vals)
            node.right = decode(vals)
            return node
        vals = iter(data.split())
        return decode(vals)

if __name__ == "__main__":
    ser = SerializeBT()
    deser = SerializeBT()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = None
    root.left.right = None
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(deser.deserialize(ser.serialize(root)))