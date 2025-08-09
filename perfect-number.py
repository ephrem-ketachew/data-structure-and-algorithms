# 507. Perfect Number
# Easy
# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

# Given an integer n, return true if n is a perfect number, otherwise return false.

# Example 1:

# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.
# Example 2:

# Input: num = 7
# Output: false

# Constraints:

# 1 <= num <= 108

from math import isqrt

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        summ = 1
        for n in range(2, isqrt(num)+ 1):
            if num % n == 0:
                d = num // n
                summ += n + (d if d != n else 0)
                
        return summ == num
    
# solution = Solution()
# num = 6
# print(solution.checkPerfectNumber(num))