# 2396. Strictly Palindromic Number
# Medium
# An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

# Given an integer n, return true if n is strictly palindromic and false otherwise.

# A string is palindromic if it reads the same forward and backward.

# Example 1:

# Input: n = 9
# Output: false
# Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
# In base 3: 9 = 100 (base 3), which is not palindromic.
# Therefore, 9 is not strictly palindromic so we return false.
# Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.
# Example 2:

# Input: n = 4
# Output: false
# Explanation: We only consider base 2: 4 = 100 (base 2), which is not palindromic.
# Therefore, we return false. 

# Constraints:

# 4 <= n <= 105

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False
        # def to_base(n, base):
        #     stack = []
        #     while n > 0:
        #         stack.append(str(n % base))
        #         n //= base 
        #     stack.reverse()
            
        #     return ''.join(stack)
        
        # def is_palindrome(n):
        #     left, right = 0, len(n) - 1
        #     while left < right:
        #         if n[left] != n[right]:
        #             return False
        #         left += 1
        #         right -= 1
                
        #     return True
        
        # for base in range(2, n - 1):
        #     num = to_base(n, base)
        #     if not is_palindrome(num):
        #         return False
            
        # return True                
                
# solution = Solution()
# n = 4
# print(solution.isStrictlyPalindromic(n))
                