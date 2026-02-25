# 50. Pow(x, n)
# Medium

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

# Constraints:

# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n is an integer.
# Either x is not zero or n > 0.
# -104 <= xn <= 104

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # exp = abs(n)
        # res = 1
        
        # for _ in range(exp):
        #     res *= x
            
        # if n < 0:
        #     res = 1 / res
            
        # return res
        
        if n < 0:
            x = 1 / x
            n = abs(n)
            
        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= x
                
            x *= x
            n //= 2
            
        return res