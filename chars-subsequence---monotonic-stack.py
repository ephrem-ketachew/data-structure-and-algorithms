# 1081. Smallest Subsequence of Distinct Characters
# Medium

# Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.
 
# Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_ocr = {ch: i for i, ch in enumerate(s)}
        seen = set()
        stack = []
        for i, ch in enumerate(s):
            if ch in seen:
                continue
            
            while stack and stack[-1] > ch and last_ocr[stack[-1]] > i:
                seen.remove(stack[-1])
                stack.pop()
                
            stack.append(ch)
            seen.add(ch)
            
        return ''.join(stack)