# Q1. Check Divisibility by Digit Sum and Product
# You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:

# The digit sum of n (the sum of its digits).

# The digit product of n (the product of its digits).

# Return true if n is divisible by this sum; otherwise, return false.

# Example 1:

# Input: n = 99

# Output: true

# Explanation:

# Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.

# Example 2:

# Input: n = 23

# Output: false

# Explanation:

# Since 23 is not divisible by the sum (2 + 3 = 5) plus product (2 * 3 = 6) of its digits (total 11), the output is false.

# Constraints:

# 1 <= n <= 106©leetcode

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ = 0
        product = 1
        
        s = str(n)
        for num in s:
            summ += int(num)
            product *= int(num)
            
        return n % (summ + product) == 0
    
# solution = Solution()
# n = 23
# print(solution.checkDivisibility(n))
            