# 392. Is Subsequence
# Easy
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
 
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True

        i = j = 0
        while i < len(t):
            if j < len(s) and t[i] == s[j]:
                j += 1
                
            if j == len(s):
                return True
            
            i += 1
        
        return False