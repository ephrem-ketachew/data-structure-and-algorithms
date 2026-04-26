# 51. N-Queens
# Hard

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

# Example 1:

# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]

# Constraints:

# 1 <= n <= 9

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # ans = []
        # def backtrack(config: List[List[str]], diagonal_cells: set[int], seen_cols: set[int]):
        #     if len(config) == n:
        #         ans.append(config[:])
        #         return
            
        #     i = len(config)
        #     for j in range(n):
        #         if j in seen_cols:
        #             continue
                
        #         if (i, j) in diagonal_cells:
        #             continue
                
        #         r, c = i, j
        #         temp = set()
        #         temp.add((i, j))
        #         while r - 1 >= 0 and c - 1 >= 0:
        #             r -= 1
        #             c -= 1
        #             temp.add((r, c))
                    
        #         r, c = i, j
        #         while r + 1 < n and c + 1 < n:
        #             r += 1
        #             c += 1
        #             temp.add((r, c))
                    
        #         r, c = i, j
        #         while r - 1 >= 0 and c + 1 < n:
        #             r -= 1
        #             c += 1
        #             temp.add((r, c))
                    
        #         r, c = i, j
        #         while r + 1 < n and c - 1 >= 0:
        #             r += 1
        #             c -= 1
        #             temp.add((r, c))
                    
        #         row = ['.'] * n
        #         row[j] = 'Q'
                
        #         seen_cols.add(j)
        #         config.append(''.join(row))
                
        #         backtrack(config, diagonal_cells | temp, seen_cols)
              
        #         seen_cols.remove(j)
        #         config.pop()
                
        # backtrack([], set(), set())
        # return ans
        
        ans = []
        def backtrack(config: List[List[str]], pos_seen: set[tuple[int, int]], neg_seen: set[tuple[int, int]], seen_col: set[int]) -> None:
            if len(config) == n:
                ans.append(config[:])
                return
            
            i = len(config)
            for j in range(n):
                if j in seen_col:
                    continue
                
                pos_id = i + j
                neg_id = i - j
                if pos_id in pos_seen or neg_id in neg_seen:
                    continue
                
                row = '.' * j + 'Q' + '.' * (n - 1 - j)
                
                config.append(row)
                pos_seen.add(pos_id)
                neg_seen.add(neg_id)
                seen_col.add(j) 
                
                backtrack(config, pos_seen, neg_seen, seen_col)
                
                config.pop()
                pos_seen.remove(pos_id)
                neg_seen.remove(neg_id)
                seen_col.remove(j)
                
        backtrack([], set(), set(), set())
        return ans