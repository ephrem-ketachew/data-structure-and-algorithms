# 37. Sudoku Solver
# Hard

# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

# Example 1:

# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """                 
  
        buckets = [[[] for _ in range(3)] for _ in range(3)]
        seen_cols = [[] for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    r, c = i // 3, j // 3
                    buckets[r][c].append(board[i][j])
                    seen_cols[j].append(board[i][j])
                     
        def backtrack(i: int, j: int) -> bool:
            if i == 9:
                return True
                
            if board[i][j] != '.':
                x, y = i + (j + 1) // 9, (j + 1) % 9
                if backtrack(x, y): 
                    return True
                return False
            
            for k in range(1, 10):
                num = str(k)
                r, c = i // 3, j // 3
                if num not in seen_cols[j] and num not in buckets[r][c] and num not in board[i]:
                    board[i][j] = num
                    seen_cols[j].append(num)
                    buckets[r][c].append(num)
                    
                    x, y = i + (j + 1) // 9, (j + 1) % 9
                    if backtrack(x, y):
                        return True
                    
                    board[i][j] = '.'
                    seen_cols[j].pop()
                    buckets[r][c].pop()
                    
            return False
             
        backtrack(0, 0)