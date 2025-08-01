# 5. Longest Palindromic Substring
# Medium
# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # max_len = 1
        # max_pal = s[0]
        
        # for i in range(len(s)):
        #     left = start = 0
        #     right = i
        #     while left <= right:
        #         if s[left] == s[right]:
        #             left += 1
        #             right -= 1
        #         else:
        #             start += 1
        #             left = start
        #             right = i
                    
        #     cur_len = i - start + 1
        #     if cur_len > max_len:
        #         max_len = cur_len
        #         max_pal = s[start:i + 1]

        # return max_pal
        
        def expand_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        max_pal = ''
        for i in range(len(s)):
            # odd_center_pal = expand_center(i, i)
            # if len(odd_center_pal) > len(max_pal):
            #     max_pal = odd_center_pal
            # even_center_pal = expand_center(i, i + 1)
            # if len(even_center_pal) > len(max_pal):
            #     max_pal = even_center_pal
            max_pal = max(max_pal, expand_center(i, i), expand_center(i, i + 1), key=len)
                
        return max_pal
            
# solution = Solution()
# s = "babad"
# s = "cbbd"
# print(solution.longestPalindrome(s))