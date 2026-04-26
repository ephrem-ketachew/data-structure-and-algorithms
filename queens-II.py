# 52. N-Queens II
# Hard
# Topics
# premium lock icon
# Companies
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

# Example 1:

# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 9

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        def backtrack(curr_len: int, pos_seen: set, neg_seen: set, col_seen: set):
            if curr_len == n:
                self.count += 1
                return
            
            i = curr_len
            for j in range(n):
                if j in col_seen:
                    continue
                
                pos_id = i + j
                neg_id = i - j
                if pos_id in pos_seen or neg_id in neg_seen:
                    continue
                
                pos_seen.add(pos_id)
                neg_seen.add(neg_id)
                col_seen.add(j)
                
                backtrack(curr_len + 1, pos_seen, neg_seen, col_seen)
                
                pos_seen.remove(pos_id)
                neg_seen.remove(neg_id)
                col_seen.remove(j)
                
        backtrack(0, set(), set(), set())
        return self.count