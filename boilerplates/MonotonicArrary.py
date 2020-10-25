"""
Given an array of integers, we would like to determine whether the array is monotonic (non-decreasing/non-increasing) or not.
Examples:
// 1 2 5 5 8
// true
// 9 4 4 2 2
// true
// 1 4 6 3
// false

//1 1 1 1 1 1
// true
"""


class Solution:
    def isMonotonic(self, arr):
        return (
            all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) or
            all(arr[i] >= arr[i+1] for i in range(len(arr)-1))
        )

    def isMonotonic(self, A):
        def cmp(a, b):
            return (a > b) - (a < b)
        store = 0
        for i in range(len(A) - 1):
            c = cmp(A[i], A[i+1])
            if c:
                if c != store != 0:
                    return False
                store = c
        return True


if __name__ == "__main__":
    s = Solution()
    assert (s.isMonotonic([1, 2, 5, 5, 8])) == True
    assert (s.isMonotonic([9, 4, 4, 2, 2])) == True
    assert (s.isMonotonic([1, 4, 6, 3])) == False
    assert (s.isMonotonic([1, 1, 1, 1, 1])) == True