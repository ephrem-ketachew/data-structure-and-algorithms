# 522. Longest Uncommon Subsequence II
# Medium
# Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.

# An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.

# A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

# For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).
 
# Example 1:

# Input: strs = ["aba","cdc","eae"]
# Output: 3
# Example 2:

# Input: strs = ["aaa","aaa","aa"]
# Output: -1

# Constraints:

# 2 <= strs.length <= 50
# 1 <= strs[i].length <= 10
# strs[i] consists of lowercase English letters.

from typing import List
from collections import Counter

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(s, string):
            i = j = 0
            while i < len(string) and j < len(s):
                if s[j] == string[i]:
                    j += 1
                i += 1
            
            return j == len(s)

        counter = Counter(strs)
        sorted_counter = sorted(counter.items(), key=lambda x: len(x[0]), reverse=True)
        for i, (s, freq) in enumerate(sorted_counter):
            if freq > 1:
                continue
            for k in range(i):
                if is_subsequence(s, sorted_counter[k][0]):
                    break
            else:
                return len(s)
            
        return -1
        
# solution = Solution()
# strs = ["aba","cdc","eae"]
# strs = ["aaa","aaa","aa"]
# print(solution.findLUSlength(strs))