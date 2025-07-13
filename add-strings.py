# 415. Add Strings
# Easy
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"

# Constraints:

# 1 <= num1.length, num2.length <= 104
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def add(s1, s2):
            carry, summ, res = 0, 0, ''
            for k in range(- 1, -len(s1)- 1, -1):
                if k < -len(s2):
                    break
                summ = int(s1[k]) + int(s2[k]) + carry
                carry = summ // 10
                if k >= -len(s2):
                    res = str(summ % 10) + res
            
            rest = ''
            for l in range(-len(s2) - 1, -len(s1)- 1, -1):
                summ = int(s1[l]) + carry
                carry = summ // 10
                rest = str(summ % 10) + rest
                
            if carry:
                rest = str(carry) + rest
            return rest + res
        
        if len(num1) >= len(num2):
            return add(num1, num2)
        else:
            return add(num2, num1)