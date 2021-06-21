"""
Given two sorted integer arrays nums1 and nums2 and return the sorted array

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to
hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = [None] * (m + n)
        i = j = k = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                result[k] = nums1[i]
                k += 1
                i += 1
            else:
                result[k] = nums2[j]
                k += 1
                j += 1

        while i < m:
            result[k] = nums1[i]
            i += 1
            k += 1

        while j < n:
            result[k] = nums2[j]
            j += 1
            k += 1

        return result

if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(s.merge(nums1, m, nums2, n))
