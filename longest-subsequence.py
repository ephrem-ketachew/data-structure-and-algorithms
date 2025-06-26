# 2311. Longest Binary Subsequence Less Than or Equal to K

# You are given a binary string s and a positive integer k.

# Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

# Note:

# The subsequence can contain leading zeroes.
# The empty string is considered to be equal to 0.
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
 

# Example 1:

# Input: s = "1001010", k = 5
# Output: 5
# Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
# Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
# The length of this subsequence is 5, so 5 is returned.
# Example 2:

# Input: s = "00101001", k = 1
# Output: 6
# Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
# The length of this subsequence is 6, so 6 is returned.
 

# Constraints:

# 1 <= s.length <= 1000
# s[i] is either '0' or '1'.
# 1 <= k <= 109

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        value = 0
        power = 1
        count = 0
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                count += 1
            else:
                if power + value <= k:
                    count += 1
                    value += power
            
            power *= 2
            if power > k:
                break
            
        for j in range(i - 1, -1 , -1):
            if s[j] == '0':
                count += 1
                
        return count
        
        # if len(s) == 1:
        #     if int(s) <= k:
        #         return 1
        #     else:
        #         return 0

        # dp = [0] * len(s)
        # if s[0] == '0':
        #     dp[0] = 1
            
        # max_length = 0
        
        # for i in range(1, len(s)):
        #     if s[i] == '0':
        #         dp[i] = dp[i - 1] + 1
        #     else:
        #         dp[i] = dp[i - 1]
              
        #     decimal = 0 
        #     j = i   
        #     length = 0
        #     power = 1
        #     while j >= 0:
        #         decimal += (int(s[j]) * power)
        #         if decimal > k:
        #             break
        #         length += 1
        #         j -= 1
        #         power *= 2
       
        #     if j > 0:
        #         length += dp[j - 1]    
        #     max_length = max(max_length, length)
            
        # return max_length
    
# s = "1001010"
# k = 5
# solution = Solution()
# print(solution.longestSubsequence(s, k))