# 1616. Split Two Strings to Make Palindrome
# Medium
# You are given two strings a and b of the same length. Choose an index and split both strings at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.

# When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.

# Return true if it is possible to form a palindrome string, otherwise return false.

# Notice that x + y denotes the concatenation of strings x and y.

# Example 1:

# Input: a = "x", b = "y"
# Output: true
# Explaination: If either a or b are palindromes the answer is true since you can split in the following way:
# aprefix = "", asuffix = "x"
# bprefix = "", bsuffix = "y"
# Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.
# Example 2:

# Input: a = "xbdef", b = "xecab"
# Output: false
# Example 3:

# Input: a = "ulacfd", b = "jizalu"
# Output: true
# Explaination: Split them at index 3:
# aprefix = "ula", asuffix = "cfd"
# bprefix = "jiz", bsuffix = "alu"
# Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.

# Constraints:

# 1 <= a.length, b.length <= 105
# a.length == b.length
# a and b consist of lowercase English letters

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def is_palindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def check(s1, s2):
            left, right = 0, len(s1) - 1
            while left < right and s1[left] == s2[right]:
                left += 1
                right -= 1
                
            if left >= right:
                return True
            
            return is_palindrome(s1, left, right) or is_palindrome(s2, left, right)
        
        return check(a, b) or check(b, a)
        
        
        # BURTE FORCE TLE
        # def is_palindrome(s, left, right):
        #     left, right = 0, len(s) - 1
        #     while left < right:
        #         if s[left] != s[right]:
        #             return False
        #         left += 1
        #         right -= 1
                
        #     return True
                
        # for i in range(len(a) + 1):
        #     a_prefix = a[:i]
        #     a_suffix = a[i:]
            
        #     b_prefix = b[:i]
        #     b_suffix = b[i:]
            
        #     if is_palindrome(a_prefix + b_suffix):
        #         return True
        #     if is_palindrome(b_prefix + a_suffix):
        #         return True
            
        # return False