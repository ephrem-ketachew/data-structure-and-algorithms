# 1446. Consecutive Characters
# Easy
# The power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Given a string s, return the power of s.

# Example 1:

# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# Example 2:

# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
 
# Constraints:

# 1 <= s.length <= 500
# s consists of only lowercase English letters.

class Solution:
    def maxPower(self, s: str) -> int:
        max_len = 1
        left = 0
        
        for right in range(1, len(s)):
            if s[right] != s[left]:
                left = right
                
            max_len = max(max_len, right - left + 1)
            
        return max_len