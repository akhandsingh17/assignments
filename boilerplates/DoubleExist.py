"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
More formally check if there exists two indices i and j such that :

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

"""


class Solution:
    def checkIfExist(self, arr) -> bool:
        dct = {}
        for idx, item in enumerate(arr):
            comp1 = item * 2
            comp2 = item / 2 if item % 2 == 0 else None
            if item in dct.keys() or comp2 in dct.items():
                return True
            else:
                dct[comp1] = idx
                dct[comp2] = idx
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.checkIfExist([10, 2, 5, 3]) == True
    assert s.checkIfExist([7, 1, 14, 11]) == True
    assert s.checkIfExist([3, 1, 7, 11]) == False
