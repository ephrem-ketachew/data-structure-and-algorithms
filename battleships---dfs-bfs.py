# 419. Battleships in a Board
# Medium

# Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

# Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

# Example 1:

# Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
# Output: 2
# Example 2:

# Input: board = [["."]]
# Output: 0
 
# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is either '.' or 'X'.
 
# Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?

from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        def sink_ships(r: int, c: int) -> None:
            if (r < 0 or r == m) or (c < 0 or c == n) or board[r][c] == '.':
                return
            
            board[r][c] = '.'
            
            sink_ships(r - 1, c)
            sink_ships(r + 1, c)
            sink_ships(r, c - 1)
            sink_ships(r, c + 1)
            
        count_ships = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    count_ships += 1
                    sink_ships(i, j)
                    
        return count_ships