"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string
Input: ["flower","flow","flight"]
Output: "fl"
"""

class Solution:
    def longestCommonPrefix(self, strs):

        longest_pre = ""
        if not strs:
            return longest_pre

        shortest_prefix = min(strs, key=len)
        for i in range(len(shortest_prefix)):
            if all([x.startswith(shortest_prefix[:i+1]) for x in strs]):
                longest_pre = shortest_prefix[:i+1]
            else:
                break
        return longest_pre

if __name__ == "__main__":
    s = Solution()
    assert (s.longestCommonPrefix(strs=["flower", "flow", "flight"])) == "fl"
    assert (s.longestCommonPrefix(strs=["dog", "racecar", "car"])) == ""
    assert (s.longestCommonPrefix(strs=["a"])) == "a"
    assert (s.longestCommonPrefix(strs=["c", "c"])) == "c"
    assert (s.longestCommonPrefix(strs=["", ""])) == ""
    assert (s.longestCommonPrefix(strs=["a", "b"])) == ""
    assert (s.longestCommonPrefix(strs=["a", "ac"])) == "a"


