# 130. Surrounded Regions
# Medium

# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

# Example 1:

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

# Explanation:


# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

# Example 2:

# Input: board = [["X"]]

# Output: [["X"]]

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def color(r: int, c: int, prev: str, target: str) -> None:
            if r == -1 or r == m or c == -1 or c == n or board[r][c] != prev:
                return
            
            board[r][c] = target
            
            color(r + 1, c, prev, target)
            color(r - 1, c, prev, target)
            color(r, c + 1, prev, target)
            color(r, c - 1, prev, target)
            
        for i in range(m):
            if board[i][0] == 'O':
                color(i, 0, 'O', 'A')
            if board[i][n - 1] == 'O':
                color(i, n - 1, 'O', 'A')
                
        for j in range(n):
            if board[0][j] == 'O':
                color(0, j, 'O', 'A')
            if board[m - 1][j] == 'O':
                color(m - 1, j, 'O', 'A')
                
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':   
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'