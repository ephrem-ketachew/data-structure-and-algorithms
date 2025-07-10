# 1234. Replace the Substring for Balanced String
# Medium
# You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.

# A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.

# Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. If s is already balanced, return 0.

# Example 1:

# Input: s = "QWER"
# Output: 0
# Explanation: s is already balanced.
# Example 2:

# Input: s = "QQWE"
# Output: 1
# Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
# Example 3:

# Input: s = "QQQW"
# Output: 2
# Explanation: We can replace the first "QQ" to "ER". 

# Constraints:

# n == s.length
# 4 <= n <= 105
# n is a multiple of 4.
# s contains only 'Q', 'W', 'E', and 'R'

from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        max_allowed = len(s) // 4
        
        if counter['Q'] == counter['W'] == counter['E'] == counter['R'] == max_allowed:
            return 0
        
        left, min_len = 0, len(s)
        for right in range(len(s)):
            counter[s[right]] -= 1
            while left <= right and counter['E'] <= max_allowed and counter['Q'] <= max_allowed and counter['R'] <= max_allowed and counter['W'] <= max_allowed:
                min_len = min(min_len, right - left + 1)
                counter[s[left]] += 1
                left += 1
                
        return min_len
    
# solution = Solution()
# s = "QWER"
# s = "QQWE"
# s = "QQQW"
# print(solution.balancedString(s))