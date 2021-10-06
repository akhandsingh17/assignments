"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = set()

        def dfs(r, c, index):
            if index == len(word):
                return True

            if r < 0 or r >= ROWS or c < 0 or c >= COLS or word[index] != board[r][c] and (r, c) in path:
                return False

            path.add((r, c))
            res = (
                   dfs(r + 1, c, index + 1) or
                   dfs(r - 1, c, index + 1) or
                   dfs(r, c + 1, index + 1) or
                   dfs(r, c - 1, index + 1))

            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(s.exist(board, word))

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    print(s.exist(board, word))
