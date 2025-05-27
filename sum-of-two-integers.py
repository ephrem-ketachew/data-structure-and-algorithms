# Sum of Two Integers

# Given two positive integers a and b, return the sum of the two integers without using the operators + and -.

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5
 

# Constraints:

# 0 <= a, b <= 1000
from collections import Counter

class Solution:
    def getSum(self, a: int, b: int) -> int:
        def get_bin(num):
            num = bin(num)
            return num[num.index('b') + 1:]
            
        a = get_bin(a)
        b = get_bin(b)
        
        max_len = max(len(a), len(b))
        a = a.rjust(max_len, '0')
        b = b.rjust(max_len, '0')
        
        result = ''
        carry = 0
        for i in range(len(a) - 1, - 1, - 1):
            my_counter = Counter([a[i], b[i], str(carry)])
            if my_counter['1'] == 0:
                result = '0' + result
                carry = 0
            elif my_counter['1'] == 1:
                result = '1' + result
                carry = 0
            elif my_counter['1'] == 2:
                result = '0' + result
                carry = 1
            else:
                result = '1' + result
                carry = 1
        if carry:
            result = '1' + result

        return int(result, 2)
        