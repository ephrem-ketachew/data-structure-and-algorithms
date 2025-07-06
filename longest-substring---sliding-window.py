# 395. Longest Substring with At Least K Repeating Characters
# Medium
# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

# if no such substring exists, return 0.

# Example 1:

# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:

# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 105

from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        count = Counter(s)
        
        for char in count:
            if count[char] < k:
                return max(self.longestSubstring(substring, k) for substring in s.split(char))
                
        return len(s)
    
        # max_len = 0
        
        # for right in range(len(s)):
        #     count = Counter()
        #     for left in range(right, -1, -1):
        #         count[s[left]] += 1
                
        #         valid = True
        #         for c in count:
        #             if count[c] < k:
        #                 valid = False
        #         if valid:
        #             max_len = max(max_len, right - left + 1)
                    
        # return max_len