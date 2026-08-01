# 761. Special Binary String
# Hard

# Special binary strings are binary strings with the following two properties:

# The number of 0's is equal to the number of 1's.
# Every prefix of the binary string has at least as many 1's as 0's.
# You are given a special binary string s.

# A move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.

# Return the lexicographically largest resulting string possible after applying the mentioned operations on the string.

# Example 1:

# Input: s = "11011000"
# Output: "11100100"
# Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
# This is the lexicographically largest string possible after some number of swaps.
# Example 2:

# Input: s = "10"
# Output: "10"

# Constraints:

# 1 <= s.length <= 50
# s[i] is either '0' or '1'.
# s is a special binary string.

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return ''
        
        components = []
        i = 0
        count = 0
        for j, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1
            
            if count == 0:
                inner_str = self.makeLargestSpecial(s[i+1:j])
                components.append('1' + inner_str + '0')
                i = j + 1
        
        components.sort(reverse=True)
        return ''.join(components)