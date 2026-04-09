# 767. Reorganize String
# Medium

# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.

from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counter = Counter(s)
        ans = [""] * n
        sorted_s = sorted(counter.items(), key=lambda x:-x[1])
        pos = 0
        for char, freq in sorted_s:
            for _ in range(freq):
                if pos >= n:
                    pos = 1
                ans[pos] = char
                pos += 2
        
        organized_str = ''.join(ans)
        for i in range(1, n):
            if organized_str[i] == organized_str[i - 1]:
                return ''    
            
        return organized_str