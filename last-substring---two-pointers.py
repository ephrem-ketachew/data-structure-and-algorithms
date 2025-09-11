# 1163. Last Substring in Lexicographical Order
# Hard
# Given a string s, return the last substring of s in lexicographical order.

# Example 1:

# Input: s = "abab"
# Output: "bab"
# Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
# Example 2:

# Input: s = "leetcode"
# Output: "tcode"
 

# Constraints:

# 1 <= s.length <= 4 * 105
# s contains only lowercase English letters.

class Solution:
    def lastSubstring(self, s: str) -> str:
        # last = ''
        # for i in range(len(s)):
        #     last = max(last, s[i:])
        # return max(last, s[i:])
        
        # max_ch = max(s)
        # last = ''
        # i = -1
        # while i < len(s):
        #     i = s.find(max_ch, i + 1)
        #     if i != -1:
        #         last = max(last, s[i:])
        #     else:
        #         break

        # return last
        
        n = len(s)
        i = k = 0
        j = 1
        while j + k < n:
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i + k] > s[j + k]:
                j = j + k + 1
                k = 0
            else:
                i = i + k + 1
                k = 0
                if i >= j:
                    j = i + 1
                    
        return s[i:]