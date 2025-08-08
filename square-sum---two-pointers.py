# 633. Sum of Square Numbers
# Medium
# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

# Example 1:

# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:

# Input: c = 3
# Output: false

# Constraints:

# 0 <= c <= 231 - 1
from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # n = int(sqrt(c)) + 1
        # for a in range(n):
        #     b = a
        #     res = 0
        #     while res <= c:
        #         res = a * a + b * b
        #         if res == c:
        #             return True
        #         b += 1
                
        # return False
        
        left = 0
        right = int(sqrt(c)) + 1
        
        while left <= right:
            res = left * left + right * right
            if res == c:
                return True
            
            if res < c:
                left += 1
            else:
                right -= 1
                
        return False
        
        # seen = set()
        # n = int(sqrt(c)) + 1
        
        # for a in range(n):
        #     seen.add(a)
        #     b = sqrt(c - a * a)
        #     if b in seen:
        #         return True
            
        # return False
    
# solution = Solution()
# c = 5
# print(solution.judgeSquareSum(c))