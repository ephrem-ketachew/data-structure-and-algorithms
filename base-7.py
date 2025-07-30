# 504. Base 7
# Easy
# Given an integer num, return a string of its base 7 representation.

# Example 1:

# Input: num = 100
# Output: "202"
# Example 2:

# Input: num = -7
# Output: "-10"

# Constraints:

# -107 <= num <= 107

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        stack = []
        if num < 0:
            sign = '-'
            num = abs(num)
        else:
            sign = ''
            
        while num > 0:
            stack.append(str(num % 7))
            num //= 7
            
        return sign + ''.join(stack[::-1])