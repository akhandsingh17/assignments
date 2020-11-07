"""
Given a list of daily temperatures T, return a list such that, for each day in the input,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.
For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0]

"""


class Solution:

    def __init__(self):
        self._data = []

    def isEmpty(self):
        return len(self._data) == 0

    def top(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        else:
            return self._data[-1]

    def push(self,item):
        self.item = item
        if self.item:
            self._data.append(item)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        else:
            return self._data.pop()

    def dailyTemperatures(self, T):
        self.T = T
        n = len(T)
        wait = [0] * n
        for i in range (n-1, -1, -1): #read the temperature array in reverse order.
            if self.isEmpty():
                self.push(i)
            else:
                while not (self.isEmpty()) and T[i] >= T[self.top()]:
                    self.pop()
                wait[i] = self.top() - i if not self.isEmpty() else 0
                self.push(i)
        return wait

if __name__ == "__main__":
    s = Solution()
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(s.dailyTemperatures(T))

