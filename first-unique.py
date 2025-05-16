# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Example 1:

# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:

# Input: s = "loveleetcode"

# Output: 2

# Example 3:

# Input: s = "aabb"

# Output: -1
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_counter = Counter(s)
        
        for index, char in enumerate(s):
            if my_counter[char] == 1:
                return index
            
        return -1