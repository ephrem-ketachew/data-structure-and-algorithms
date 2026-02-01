# 316. Remove Duplicate Letters
# Medium

# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results. 

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.

# Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
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