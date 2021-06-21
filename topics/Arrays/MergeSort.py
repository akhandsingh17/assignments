"""
Merge two sorted arrays
Input: arr1[] = { 1, 3, 4, 5}, arr2[] = {2, 4, 6, 8}
Output: arr3[] = {1, 2, 3, 4, 4, 5, 6, 8}

"""

class MergeSort:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def merge(self):
        l1, l2 = len(self.list1), len(self.list2)
        result = [None] * (l1 + l2)
        i, j, k = 0, 0, 0
        while i < l1 and j < l2:
            if self.list1[i] < self.list2[j]:
                result[k] = self.list1[i]
                k += 1
                i += 1
            else:
                result[k] = self.list2[j]
                k += 1
                j += 1

        while i < l1:
            result[k] = self.list1[i]
            k += 1
            i += 1
        while j < l2:
            result[k] = self.list2[j]
            k += 1
            j += 1
        print(result)


if __name__ == "__main__":
    s = MergeSort([1, 3, 4, 5], [2, 4, 6, 8, 12])
    s.merge()