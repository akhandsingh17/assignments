"""
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = 0
        maxLength = 0  # result
        unique = set()
        while end < len(s):
            if s[end] not in unique:
                unique.add(s[end])
                end += 1
                maxLength = max(maxLength, len(unique))
            else:
                unique.remove(s[start])
                start += 1
        return maxLength


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))