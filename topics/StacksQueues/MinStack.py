"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minEle = None

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, val: int) -> None:
        if self.isEmpty():
            self.minEle = val

        if self.minEle <= val:
            self.stack.append(val)
        else:
            self.stack.append((2 * val) - self.minEle)
            self.minEle = val

    def pop(self) -> None:
        if self.isEmpty():
            raise "stack is empty!"

        if self.stack[-1] >= self.minEle:
            self.stack.pop()
        else:
            self.minEle = (2 * self.minEle) - self.stack[-1]
            self.stack.pop()

        self.minEle = None if self.isEmpty() else self.minEle

    def top(self) -> int:
        if self.isEmpty():
            raise "stack is empty"
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minEle


if __name__ == "__main__":
    minStack = MinStack()
    op_types = ["push", "push", "push", "top", "pop", "getMin", "pop", "getMin", "pop", "push", "top",
                "getMin", "push", "top", "getMin", "pop", "getMin"]
    op_vals = [[2147483646], [2147483646], [2147483647], [], [], [], [], [], [], [2147483647], [], [], [-2147483648],
               [], [], [], []]
    for idx, op_type in enumerate(op_types):
        if op_type == "push":
            print(eval("minStack." + op_type + "(" + str(op_vals[idx][0]) + ")"))
        else:
            print(eval("minStack." + op_type + "()"))
