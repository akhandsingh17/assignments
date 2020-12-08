"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.
For example,

[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the data structure.
    double findMedian() - Return the median of all elements so far.



Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


"""
from queue import PriorityQueue

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller = PriorityQueue() # max heap
        self.greater = PriorityQueue() # min heap
        self.med = None

    def addNum(self, num: int) -> None:
        if self.med is None:
            self.med = num
            self.smaller.put(-1 * num)
        else:
            if self.smaller.qsize() > self.greater.qsize():
                if num < self.med:
                    self.greater.put(-1 * self.smaller.get())
                    self.smaller.put(-1 * num)
                else:
                    self.greater.put(num)
                self.med = ((-1 * self.smaller.queue[0]) + self.greater.queue[0]) / 2

            elif self.greater.qsize() == self.smaller.qsize():
                if num < self.med:
                    self.smaller.put(-1 * num)
                    self.med = -1 * self.smaller.queue[0]
                else:
                    self.greater.put(num)
                    self.med = self.greater.queue[0]

            else:
                if num > self.med:
                    self.smaller.put(-1 * self.greater.get())
                    self.greater.put(num)
                else:
                    self.smaller.put(-1 * num)
                self.med = ((-1 * self.smaller.queue[0]) + self.greater.queue[0]) / 2

    def findMedian(self) -> float:
        return self.med


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

def main():
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    assert obj.findMedian() == 1.5
    obj.addNum(3)
    assert obj.findMedian() == 2

if __name__=='__main__':
    main()
