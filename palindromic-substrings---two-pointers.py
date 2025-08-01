# 647. Palindromic Substrings
# Medium
# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.

class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            length = right - left - 1
            return length // 2 if length % 2 == 0 else length // 2 + 1
        
        count = 0
        for i in range(len(s)):
            count += expand_center(i, i) + expand_center(i, i + 1)
            
        return count
    
solution = Solution()
s = "aabaa"
print(solution.countSubstrings(s))