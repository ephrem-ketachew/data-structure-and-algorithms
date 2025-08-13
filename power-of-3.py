# 326. Power of Three
# Easy
# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

# Example 1:

# Input: n = 27
# Output: true
# Explanation: 27 = 33
# Example 2:

# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.
# Example 3:

# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).
 
# Constraints:

# -231 <= n <= 231 - 1

# Follow up: Could you solve it without loops/recursion?

from math import log

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        
        # num = 1
        # while num <= n:
        #     if num == n:
        #         return True
        #     num *= 3
        
        # return False
        
        # def __is_power_of_three(num):
        #     if num == 1:
        #         return True
        #     elif num < 1 or num % 3:
        #         return False
        #     num //= 3
        #     return __is_power_of_three(num)
        
        # return __is_power_of_three(n)
        
        UPPER_LIMIT = 2 ** 31
        MAX_EXPONENET_OF_3 = int(log(UPPER_LIMIT) / log(3))
        MAX_POWER_OF_3 = 3 ** MAX_EXPONENET_OF_3
        
        return n > 0 and MAX_POWER_OF_3 % n == 0