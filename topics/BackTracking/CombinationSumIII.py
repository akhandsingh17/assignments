"""
ind all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.



Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
Example 4:

Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.
Example 5:

Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
There are no other valid combinations.

"""

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        candidates = [i for i in range(1, 10)]

        if k * (k + 1) // 2 > n:
            return res

        def dfs(i, curr, total):
            if total == n and len(curr) == k:
                res.append(curr.copy())
                return

            if i >= len(candidates) or total > n or len(curr) > k:
                return

            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res


if __name__ == '__main__':
    s = Solution()
    assert (s.combinationSum3(k=3, n=7)) == [[1, 2, 4]]
    assert (s.combinationSum3(k=3, n=9)) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    assert (s.combinationSum3(k=4, n=1)) == []
    assert (s.combinationSum3(k=3, n=2)) == []
    assert s.combinationSum3(k=9, n=45) == [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
