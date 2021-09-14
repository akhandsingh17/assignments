"""
Given k sorted arrays of possibly different sizes, merge them and print the sorted output.


Input: k = 3
      arr[][] = { {1, 3},
                  {2, 4, 6},
                  {0, 9, 10, 11}} ;
Output: 0 1 2 3 4 6 9 10 11

"""
from queue import PriorityQueue


class QNode:
    def __init__(self, arr_idx, element_idx, val):
        self.arr_idx = arr_idx
        self.element_idx = element_idx
        self.val = val

    def __str__(self):
        return 'QNode <{}-{}-{}>'.format(self.arr_idx, self.element_idx, self.val)

    def __lt__(self, other):
        return self.val < other.val

    def __le__(self, other):
        return self.val <= other.val

    def __eq__(self, other):
        return self.val == other.val

    def __ne__(self, other):
        return self.val != other.val

    def __gt__(self, other):
        return self.val > other.val

    def __ge__(self, other):
        return self.val >= other.val


class MergeKSortedList:
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k

    def merge(self):
        pq = PriorityQueue()
        result = []

        for i in range(self.k):
            if len(arr[i]) > 0:
                pq.put(QNode(i, 0, arr[i][0]))

        while pq.qsize() > 0:
            qNode = pq.get()
            result.append(qNode.val)
            newIndex = qNode.element_idx + 1
            if newIndex < len(arr[qNode.arr_idx]):
                pq.put(QNode(qNode.arr_idx, newIndex, arr[qNode.arr_idx][newIndex]))
        return result


if __name__ == "__main__":
    arr = [[2, 6, 12],
           [1, 9],
           [23, 34, 90, 2000]]
    k = 3
    s = MergeKSortedList(arr=arr, k=k)
    assert s.merge() == [1, 2, 6, 9, 12, 23, 34, 90, 2000]
