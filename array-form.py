# 989. Add to Array-Form of Integer
# Easy
# The array-form of an integer num is an array representing its digits in left to right order.

# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

# Example 1:

# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234
# Example 2:

# Input: num = [2,7,4], k = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455
# Example 3:

# Input: num = [2,1,5], k = 806
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021

# Constraints:

# 1 <= num.length <= 104
# 0 <= num[i] <= 9
# num does not contain any leading zeros except for the zero itself.
# 1 <= k <= 104

from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        k_str = str(k)
        i, j, carry = len(num) - 1, len(k_str) - 1, 0
        result = [0] * len(num)
        
        while i >= 0 or j >=0 or carry > 0:
            num1 = num[i] if i >= 0 else 0
            num2 = int(k_str[j]) if j >= 0 else 0
            res = (num1 + num2 + carry) % 10
            carry = (num1 + num2 + carry) // 10
            
            if i >= 0:
                result[i] = res
            else:
                result = [res] + result
                
            i -= 1
            j -= 1
                
        return result