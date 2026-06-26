# 459. Repeated Substring Pattern
# Easy

# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s) // 2):
            token = s[:i + 1]
            times = len(s) // token
            if len(token) * times == len(s):
                if s == token * times:
                    return True
                
        return False