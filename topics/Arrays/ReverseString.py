"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
extra memory.

You may assume all the characters consist of printable ascii characters.

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

"""

class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left = 0
        right = len(s) - 1
        while left <= right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        return s

if __name__ == "__main__":
    s = Solution()
    assert (s.reverseString(["h", "e", "l", "l", "o"])) == ["o", "l", "l", "e", "h"]
    assert (s.reverseString(["H","a","n","n","a","h"])) == ["h","a","n","n","a","H"]