"""
Given a fixed length array arr of integers, duplicate each occurrence of zero,
shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your
function.

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

hint -
Identify the correct shift distance
The duplication of a zero pushes all elements to the right of it by one.
This means also that every element is shifted to the right as many times as there are zeroes to the left of it.
E.g. in the array [1,0,2,0,3] , 1 will not move, 2 will shift one position and 3 will shift two positions.
As we go backwards, every time we bypass a zero (and duplicate it), the shift distance decreases for the elements
we haven't shifted yet, because there is one less zero in front of them.
"""

class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = arr.count(0)
        for i in range(n-1, -1, -1):
            if (i + zeros) < n:
                arr[i+zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if (i + zeros) < n:
                    arr[i+zeros] = 0
        return arr


if __name__ == "__main__":
    s = Solution()
    print(s.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
