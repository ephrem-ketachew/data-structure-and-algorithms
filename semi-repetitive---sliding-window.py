# 2730. Find the Longest Semi-Repetitive Substring
# Medium
# You are given a digit string s that consists of digits from 0 to 9.

# A string is called semi-repetitive if there is at most one adjacent pair of the same digit. For example, "0010", "002020", "0123", "2002", and "54944" are semi-repetitive while the following are not: "00101022" (adjacent same digit pairs are 00 and 22), and "1101234883" (adjacent same digit pairs are 11 and 88).

# Return the length of the longest semi-repetitive substring of s.

# Example 1:

# Input: s = "52233"

# Output: 4

# Explanation:

# The longest semi-repetitive substring is "5223". Picking the whole string "52233" has two adjacent same digit pairs 22 and 33, but at most one is allowed.

# Example 2:

# Input: s = "5494"

# Output: 4

# Explanation:

# s is a semi-repetitive string.

# Example 3:

# Input: s = "1111111"

# Output: 2

# Explanation:

# The longest semi-repetitive substring is "11". Picking the substring "111" has two adjacent same digit pairs, but at most one is allowed.

# Constraints:

# 1 <= s.length <= 50
# '0' <= s[i] <= '9'

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left, max_len = 0, 1
        
        duplicated = False
        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                if duplicated:
                    while s[left] != s[left + 1]:
                        left += 1
                    left += 1
                else:
                    duplicated = True
            max_len = max(max_len, right - left + 1)
            
        return max_len
    
# solution = Solution()
# s = "52233"
# s = "5494"
# s = "1111111"
# print(solution.longestSemiRepetitiveSubstring(s))