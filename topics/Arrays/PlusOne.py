"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
"""
class Solution:
    def plusOne(self, digits):
        result = []
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            val = digits[i] + carry
            carry = int(val/10)
            result.append(val % 10)
        if carry > 0:
            result.append(carry)
        result.reverse()
        return result

def main():
    s = Solution()
    assert (s.plusOne([1, 0, 9])) == [1, 1, 0]
    assert (s.plusOne([1, 9, 9])) == [2, 0, 0]
    assert (s.plusOne([9, 0, 9])) == [9, 1, 0]
    assert (s.plusOne([1, 1, 0])) == [1, 1, 1]
    assert (s.plusOne([9, 9, 9])) == [1, 0, 0, 0]

if __name__=='__main__':
    main()