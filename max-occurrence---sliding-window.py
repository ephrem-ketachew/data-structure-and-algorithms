# 1297. Maximum Number of Occurrences of a Substring
# Medium
# Given a string s, return the maximum number of occurrences of any substring under the following rules:

# The number of unique characters in the substring must be less than or equal to maxLetters.
# The substring size must be between minSize and maxSize inclusive.
 
# Example 1:

# Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
# Output: 2
# Explanation: Substring "aab" has 2 occurrences in the original string.
# It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
# Example 2:

# Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
# Output: 2
# Explanation: Substring "aaa" occur 2 times in the string. It can overlap.

# Constraints:

# 1 <= s.length <= 105
# 1 <= maxLetters <= 26
# 1 <= minSize <= maxSize <= min(26, s.length)
# s consists of only lowercase English letters.

from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counter = defaultdict(int)
        
        for i in range(len(s) - minSize + 1):
            win_str = s[i:i + minSize]
            if len(set(win_str)) <= maxLetters:
                counter[win_str] += 1
                
        return max(counter.values()) if counter else 0