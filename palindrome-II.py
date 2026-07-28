# 3517. Smallest Palindromic Rearrangement I
# Medium

# You are given a palindromic string s.

# Return the lexicographically smallest palindromic permutation of s.

# Example 1:

# Input: s = "z"

# Output: "z"

# Explanation:

# A string of only one character is already the lexicographically smallest palindrome.

# Example 2:

# Input: s = "babab"

# Output: "abbba"

# Explanation:

# Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.

# Example 3:

# Input: s = "daccad"

# Output: "acddca"

# Explanation:

# Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# s is guaranteed to be palindromic.

from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counter = Counter(s)
        half_s = []
        middle = ''
        for char in counter:
            half_s.append(char * (counter[char] // 2))
            if counter[char] % 2 == 1:
                middle = char
                
        half_s.sort()
        small_s = ''.join(half_s)
        small_s += middle
        half_s.reverse()
        small_s += ''.join(half_s)
        
        return small_s