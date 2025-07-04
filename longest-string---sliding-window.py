# 1763. Longest Nice Substring
# Easy

# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

# Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

# Example 1:

# Input: s = "YazaAay"
# Output: "aAa"
# Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
# "aAa" is the longest nice substring.
# Example 2:

# Input: s = "Bb"
# Output: "Bb"
# Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
# Example 3:

# Input: s = "c"
# Output: ""
# Explanation: There are no nice substrings.

# Constraints:

# 1 <= s.length <= 100
# s consists of uppercase and lowercase English letters.

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # a brute force approach(since the constraint is very small(100))
        # longest_string = ''
        
        # for i in range(len(s)):
        #     substring = s[i]
        #     seen = set(s[i])
        #     for j in range(i + 1, len(s)):
        #         substring += s[j]
        #         isNice = True
        #         seen.add(s[j])
        #         for k in range(len(substring)):
        #             opp_case = substring[k].upper() if substring[k].islower() else substring[k].lower()
        #             if not opp_case in seen:
        #                 isNice = False
        #                 break
                    
        #         if isNice and len(substring) > len(longest_string):
        #             longest_string = substring
                    
        # return longest_string
        
        # an optimized solution with divide and conquer strategy
        
        if len(s) < 2:
            return ""
        
        chars = set(s)
        
        for i, c in enumerate(s):
            if c.swapcase() not in chars:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                return left if len(left) >= len(right) else right
            
        return s
    
    
        # tried sliding window.........but i far i see there is no legitimate way this question can be solved through sliding window..... it's misleading..... i wasted some time
        # left = 0
        # seen = set()
        # longest_string = window = ''
        # for right in range(len(s)):
        #     opp_case = s[right].upper() if s[right].islower() else s[right].lower()
        #     if opp_case in window:
        #         window += s[right]
        #         if len(window) > len(longest_string):
        #             longest_string = window
        #     else:
        #         if len(window) > 1 and opp_case in seen:
        #             found = False
        #             for i in range(left - 1, -1, -1):
        #                 if s[i] == opp_case:
        #                     found = True
        #                 if s[i] != s[right] and s[i] != opp_case:
        #                     break 
        #             if found:
        #                 left = i + 1
        #                 window = s[left: right + 1]
        #                 if len(window) > len(longest_string):
        #                     longest_string = window
        #             else:
        #                 window = s[right]
        #                 left = right 
        #         else:
        #             window = s[right]
        #             left = right 
        #     seen.add(s[right])
            
        # return longest_string
            
# solution = Solution()
# s = "YazaAay"
# s = "Bb"
# s = "c"
# s = "jcJ"
# s = "cChH"
# print(solution.longestNiceSubstring(s))