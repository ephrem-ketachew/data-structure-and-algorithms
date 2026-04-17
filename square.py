# 279. Perfect Squares
# Medium

# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

# Constraints:

# 1 <= n <= 104

from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        queue = deque()
        seen = set()
        i = 1
        while i * i <= n:
            squares.append(i * i)
            queue.append(i * i)
            seen.add(i * i)
            i += 1
            
        count = 0
        while queue:
            t = len(queue)
            for _ in range(t):
                curr = queue.popleft()
                if curr == n:
                    return count + 1
                
                for num in squares:
                    res = curr + num
                    if res <= n and res not in seen:
                        queue.append(res)
                        seen.add(res)
                        
            count += 1
            
        return count