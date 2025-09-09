# 2443. Sum of Number and Its Reverse
# Medium
# Given a non-negative integer num, return true if num can be expressed as the sum of any non-negative integer and its reverse, or false otherwise.

# Example 1:

# Input: num = 443
# Output: true
# Explanation: 172 + 271 = 443 so we return true.
# Example 2:

# Input: num = 63
# Output: false
# Explanation: 63 cannot be expressed as the sum of a non-negative integer and its reverse so we return false.
# Example 3:

# Input: num = 181
# Output: true
# Explanation: 140 + 041 = 181 so we return true. Note that when a number is reversed, there may be leading zeros.

# Constraints:

# 0 <= num <= 105

class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        # for n in range(num // 2 + 1):
        #     comp = num - n
        #     str_n = str(n)
        #     str_comp = str(comp)

        #     l = len(str_comp) - len(str_n)
        #     str_n = '0' * l + str_n

        #     for i in range(len(str_n)):
        #         if str_n[i] != str_comp[len(str_n) - 1 - i]:
        #             break
        #     else:
        #         return True
                
        # return False
        
        for n in range(num // 2 + 1):
            rev_n = int(str(n)[::-1])
            if n + rev_n == num:
                return True
            
        return False
            