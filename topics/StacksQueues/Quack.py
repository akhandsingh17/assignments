class Quack:
    def __init__(self):
        self.right = []
        self.left = []
        self.buffer = []

    def push(self, x):
        self.left.append(x)

    def pop(self):
        if not self.left and not self.right:
            raise IndexError('pop from empty quack')

        if not self.left:  # Re-balance stacks
            size = len(self.right)
            # Move half of right stack to buffer
            for _ in range(size // 2):
                self.buffer.append(self.right.pop())
            # Move remainder of right to left
            while self.right:
                self.left.append(self.left.pop())
            # Move buffer elements back to right
            while self.buffer:
                self.right.append(self.buffer.pop())

        return self.left.pop()

    def pull(self):
        if not self.left and not self.right:
            raise IndexError('pull from empty quack')

        if not self.right:  # Re-balance stacks
            size = len(self.left)
            # Move half of left stack to buffer
            for _ in range(size // 2):
                self.buffer.append(self.left.pop())
            # Move remainder of left to right
            while self.left:
                self.right.append(self.left.pop())
            # Move buffer elements back to left
            while self.buffer:
                self.left.append(self.buffer.pop())

        return self.right.pop()