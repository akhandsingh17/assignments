'''
Problem Description
Write a function to crush candy in a one dimensional board.
In candy crushing games, groups of like items are removed from the board. In this problem, any sequence of 3 or more
like items should be removed and any items adjacent to that sequence should now be considered adjacent to each other.
This process should be repeated as many times as possible.
Sample inputs - Expected outputs
ABBBCC -> ACC
ABCCCBB -> A

'''


class Stack:
    def __init__(self):
        self._slist = []

    def isEmpty(self):
        return len(self._slist) == 0

    def top(self):
        if self.isEmpty():
            raise "Stack is Empty"
        else:
            return self._slist[-1]

    def push(self, item):
        self.item = item
        if self.item:
            self._slist.append(item)

    def pop(self):
        if self.isEmpty():
            raise "Stack is Empty"
        else:
            return self._slist.pop()


class CandyCrusher:
    def __init__(self):
        self.frequency = {}
        self.stack = Stack()
        self.result = ''

    def crushit(self, s):

        # build a hash map with frequency
        for char in s:
            if char in self.frequency.keys():
                self.frequency[char] = self.frequency.get(char) + 1
            else:
                self.frequency[char] = 1
        self.frequency

        for char in s:
            if self.frequency[char] < 3:
                self.stack.push(char)

        while not self.stack.isEmpty():
            self.result += self.stack.pop()
        return self.result[::-1]


if __name__ == "__main__":
    s = CandyCrusher()
    print(s.crushit(s='ABBBCC'))

    s = CandyCrusher()
    print(s.crushit(s='ABCCCBB'))

    s = CandyCrusher()
    print(s.crushit(s='AABCCCDDDDDBBA'))

    s = CandyCrusher()
    print(s.crushit(s='AABBBACCDDDDC'))
