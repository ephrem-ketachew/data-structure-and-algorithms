# 3713. Longest Balanced Substring I
# Medium

# You are given a string s consisting of lowercase English letters.

# A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

# Return the length of the longest balanced substring of s.

# Example 1:

# Input: s = "abbac"

# Output: 4

# Explanation:

# The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

# Example 2:

# Input: s = "zzabccy"

# Output: 4

# Explanation:

# The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly 1 time.​​​​​​​

# Example 3:

# Input: s = "aba"

# Output: 2

# Explanation:

# ​​​​​​​One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.

from collections import Counter

class Solution:
    def longestBalanced(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            counter = Counter()
            for j in range(i, len(s)):
                counter[s[j]] += 1
                if len(set(counter.values())) == 1:
                    max_len = max(max_len, j - i + 1)
                
        return max_len