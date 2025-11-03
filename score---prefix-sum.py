# 3707. Equal Score Substrings
# Easy

# You are given a string s consisting of lowercase English letters.

# The score of a string is the sum of the positions of its characters in the alphabet, where 'a' = 1, 'b' = 2, ..., 'z' = 26.

# Determine whether there exists an index i such that the string can be split into two non-empty substrings s[0..i] and s[(i + 1)..(n - 1)] that have equal scores.

# Return true if such a split exists, otherwise return false.


# Example 1:

# Input: s = "adcb"

# Output: true

# Explanation:

# Split at index i = 1:

# Left substring = s[0..1] = "ad" with score = 1 + 4 = 5
# Right substring = s[2..3] = "cb" with score = 3 + 2 = 5
# Both substrings have equal scores, so the output is true.

# Example 2:

# Input: s = "bace"

# Output: false

# Explanation:​​​​​​

# ​​​​​​​No split produces equal scores, so the output is false.

# Constraints:

# 2 <= s.length <= 100
# s consists of lowercase English letters.

class Solution:
    def scoreBalance(self, s: str) -> bool:
        summ = sum(ord(ch) - 96 for ch in s)
        prefix = 0
        for i in range(len(s)):
            prefix += ord(s[i]) - 96
            if summ - prefix == prefix:
                return True
            
            if prefix > summ - prefix:
                return False
            
        return False