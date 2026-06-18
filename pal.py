# 409. Longest Palindrome
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.

from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1
            
        count = 0
        for ch in freq:
            count += 2 * (freq[ch] // 2)
            
        if count < len(s):
            count += 1
            
        return count