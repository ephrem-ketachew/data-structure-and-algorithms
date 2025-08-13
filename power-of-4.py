# 342. Power of Four
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

# Example 1:

# Input: n = 16
# Output: true
# Example 2:

# Input: n = 5
# Output: false
# Example 3:

# Input: n = 1
# Output: true
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?

from math import log

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        
        # num = 1
        # while num <= n:
        #     if num == n:
        #         return True
        #     num *= 4
        
        # return False
        
        # def __is_power_of_three(num):
        #     if num == 1:
        #         return True
        #     elif num < 1 or num % 4:
        #         return False
        #     num //= 4
        #     return __is_power_of_three(num)
        
        # return __is_power_of_three(n)
        
        return n > 0 and log(n, 4).is_integer()
        
solution = Solution()
print(solution.isPowerOfFour(2))