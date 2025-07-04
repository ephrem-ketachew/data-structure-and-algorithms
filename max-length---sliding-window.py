# 3090. Maximum Length Substring With Two Occurrences
# Easy
# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.

# Example 1:

# Input: s = "bcbbbcba"

# Output: 4

# Explanation:

# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
# Example 2:

# Input: s = "aaaa"

# Output: 2

# Explanation:

# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".

# Constraints:

# 2 <= s.length <= 100
# s consists only of lowercase English letters.

from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)
        
        max_len = 2
        left = 0
        window_counter = Counter(s[:2])
        
        for right in range(2, len(s)):
            window_counter[s[right]] += 1
            while window_counter[s[right]] > 2:
                window_counter[s[left]] -= 1
                if window_counter[s[left]] == 0:
                    del window_counter[s[left]]
                left += 1
            max_len = max(max_len, right - left + 1)
            
        return max_len