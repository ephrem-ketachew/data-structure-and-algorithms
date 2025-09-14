# 1781. Sum of Beauty of All Substrings
# Medium
# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

# For example, the beauty of "abaacc" is 3 - 1 = 2.
# Given a string s, return the sum of beauty of all of its substrings.

# Example 1:

# Input: s = "aabcb"
# Output: 5
# Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
# Example 2:

# Input: s = "aabcbaa"
# Output: 17

# Constraints:

# 1 <= s.length <= 500
# s consists of only lowercase English letters.
from collections import Counter

class Solution:
    def beautySum(self, s: str) -> int:
        # summ = 0
        # for i in range(len(s) - 2):
        #     for j in range(i + 2, len(s)):
        #         word = s[i:j + 1]
        #         vals = Counter(word).values()
        #         summ += max(vals) - min(vals)
                
        # return summ
        
        total_beauty = 0
        n = len(s)
        for i in range(n):
            freqs = [0] * 26
            for j in range(i, n):
                freqs[ord(s[j]) - ord('a')] += 1
                
                max_freq, min_freq = 0, float('inf')
                for k in range(26):
                    if freqs[k] > 0:
                        max_freq = max(max_freq, freqs[k])
                        min_freq = min(min_freq, freqs[k])
                    
                total_beauty += max_freq - min_freq
            
        return total_beauty