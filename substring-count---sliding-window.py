# 1513. Number of Substrings With Only 1s
# Medium
# Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7. 

# Example 1:

# Input: s = "0110111"
# Output: 9
# Explanation: There are 9 substring in total with only 1's characters.
# "1" -> 5 times.
# "11" -> 3 times.
# "111" -> 1 time.
# Example 2:

# Input: s = "101"
# Output: 2
# Explanation: Substring "1" is shown 2 times in s.
# Example 3:

# Input: s = "111111"
# Output: 21
# Explanation: Each substring contains only 1's characters.

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '0' or '1'.

class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        count = 0
        left = None
        for right in range(len(s)):
            if s[right] == '1':
                if left is None:
                    left = right
                count += right - left + 1
            else:
                left = None
                
        return count % MOD
                