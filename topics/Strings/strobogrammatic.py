"""
Given a string num which represents an integer, return true if num is a strobogrammatic number.
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
Example 4:

Input: num = "1"
Output: true
"""

class Solution:
    def isstrobogrammatic(self, num):
        result = []
        temp = num
        strobogrammatic_num = {1: 1, 0: 0, 6: 9, 9: 6, 8: 8}
        while temp != 0:
            carry = (int(temp) % 10)
            if carry in strobogrammatic_num.keys():
                temp = int(temp) // 10
                result.append(str(strobogrammatic_num.get(carry)))
                continue
            else:
                return False
        return ''.join(result) == num

if __name__ == "__main__":
    s = Solution()
    assert  s.isstrobogrammatic(num='69') == True
    assert  s.isstrobogrammatic(num='88') == True
    assert  s.isstrobogrammatic(num='1') == True
    assert  s.isstrobogrammatic(num='962') == False
    assert  s.isstrobogrammatic(num='6') == False