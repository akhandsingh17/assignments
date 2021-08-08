"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half
and b be the second half.
Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice
that s contains uppercase and lowercase letters.
Return true if a and b are alike. Otherwise, return false.

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        vowel = ('a', 'e', 'i', 'o', 'u')
        first = s[:mid].lower()
        second = s[mid:].lower()
        count1, count2 = 0, 0
        for c in first:
            if c in vowel:
                count1 += 1
        for c in second:
            if c in vowel:
                count2 += 1
        return count1 == count2


if __name__ == "__main__":
    s = Solution()
    assert s.halvesAreAlike(s='textbook') == False
    assert s.halvesAreAlike(s='AbCdEfGh') == True
    assert s.halvesAreAlike(s="MerryChristmas") == False
