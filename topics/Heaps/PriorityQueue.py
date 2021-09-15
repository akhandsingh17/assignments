
from queue import PriorityQueue

class MedianMaintain:
    def __init__(self, arr):
        self.arr = arr

    def MedianFinder(self):
        med = self.arr[0]

        smaller = PriorityQueue()
        greater = PriorityQueue()

        smaller.put(-1 * self.arr[0])
        print("Median {}".format(med))

        for i in range(1, len(self.arr)):
            x = self.arr[i]

            if smaller.qsize() > greater.qsize():
                if x < med:
                    greater.put(-1 * smaller.get())
                    smaller.put(-1 * x)
                else:
                    greater.put(x)
                med = ((-1 * smaller.queue[0]) + greater.queue[0]) / 2

            elif greater.qsize() == smaller.qsize():
                if x < med:
                    smaller.put(-1 * x)
                    med = -1 * smaller.queue[0]
                else:
                    greater.put(x)
                    med = greater.queue[0]

            else:
                if x > med:
                    smaller.put(-1 * greater.get())
                    greater.put(x)
                else:
                    smaller.put(-1 * x)
                med = ((-1 * smaller.queue[0]) + greater.queue[0]) / 2

            print("Median {}:".format(med))


if __name__=='__main__':
    arr = [5, 15, 10, 20, 3]
    s = MedianMaintain(arr)
    (s.MedianFinder())