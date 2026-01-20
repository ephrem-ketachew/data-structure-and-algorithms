# 405. Convert a Number to Hexadecimal
# Easy

# Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

# All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

# Note: You are not allowed to use any built-in library method to directly solve this problem.

# Example 1:

# Input: num = 26
# Output: "1a"
# Example 2:

# Input: num = -1
# Output: "ffffffff"

# Constraints:

# -231 <= num <= 231 - 1

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
            
        MAX_NUM = 2 ** 32
        if num < 0:
            num = MAX_NUM + num
            
        hex = []
        while num > 0:
            r = num % 16
            num //= 16
            if r < 10:
                hex.append(str(r))
            else:
                hex.append(chr(97 + (r - 10)))
                
        hex.reverse()
             
        return ''.join(hex)