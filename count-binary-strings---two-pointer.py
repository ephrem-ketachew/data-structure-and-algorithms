# 696. Count Binary Substrings
# Easy
# Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

# Substrings that occur multiple times are counted the number of times they occur. 

# Example 1:

# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
# Example 2:

# Input: s = "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '0' or '1'.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        left = start1 = start2 = 0
        
        for right in range(1, len(s)):
            if s[right] != s[right - 1]:
                left = right - 1
                count += 1
                start1 = start2
                start2 = right
                
            elif left > start1:
                count += 1
                left -= 1
                
        return count
    
# solution = Solution()
# s = '0000111100011'
# s = "00110011"
# s = "10101"
# s = "00100"
# print(solution.countBinarySubstrings(s))
            