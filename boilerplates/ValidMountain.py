"""
Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:

Input: arr = [3,5,5]
Output: false

Input: arr = [0,3,2,1]
Output: true

"""

class Solution:
    def validMountainArray(self, arr) -> bool:
        if len(arr) < 3:
            return False
        top = 0
        while top + 1 < len(arr) and arr[top] < arr[top+1]:
            top += 1
        print(top)
        return all(arr[i] < arr[i+1] for i in range(top-1)) and all(arr[i] > arr[i+1] for i in range(top, len(arr) - 1))

if __name__ == "__main__":
    s = Solution()
    print(s.validMountainArray([0, 3, 2, 1]))
    print(s.validMountainArray([3, 5, 5]))
    print(s.validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))