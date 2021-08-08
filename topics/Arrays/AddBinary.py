"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
Simply put ; calculate the sum of two integers without using sum operator
"""
import typing 

class Solution:
    def addBinary(self, a: str, b: str):
        x, y = int(a, 2), int(b, 2)
        while y:
            ans = x ^ y       # Bitwise OR
            carry = (x & y) << 1
            x, y = ans, carry
        return bin(x)[2:]

if __name__ == "__main__":
    s = Solution()
    assert (s.addBinary("11", "1")) == "100"
    assert (s.addBinary("1010", "1011")) == "10101"
