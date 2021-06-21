"""
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack, needle):
        k = len(needle)
        if not needle:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i + k] == needle:
                return i
        return -1

if __name__ == "__main__":
    s = Solution()
    assert (s.strStr(haystack="hello", needle="ll")) == 2
    assert (s.strStr(haystack="aaaaa", needle="bba")) == -1
    assert (s.strStr(haystack="aaaaa", needle="")) == 0