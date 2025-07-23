# 917. Reverse Only Letters
# Easy
# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

# Example 1:

# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

# Constraints:

# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\"' or '\\'.

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s) - 1
        
        s_list = list(s)
        while left < right:
            while left < len(s_list) and not s_list[left].isalpha():
                left += 1
                
            while right >= 0 and not s_list[right].isalpha():
                right -= 1
                
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                
            left += 1
            right -= 1
                
        return ''.join(s_list)
        