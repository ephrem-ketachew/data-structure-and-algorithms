# 79. Word Search
# Medium

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.

# Follow up: Could you use search pruning to make your solution faster with a larger board?

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        path = set()
        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            
            if r == -1 or r == m or c == -1 or c == n or (r, c) in path or board[r][c] != word[i]:
                return False
            
            path.add((r, c))
            res = dfs(r + 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c - 1, i + 1)
            path.remove((r, c))
            
            return res
        
        for i in range(m):
            for j in range(n):
                res = dfs(i, j, 0)
                if res:
                    return True
                
        return False
                