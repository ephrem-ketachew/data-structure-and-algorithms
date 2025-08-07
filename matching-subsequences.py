# 792. Number of Matching Subsequences
# Medium
# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".

# Example 1:

# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
# Example 2:

# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2

# Constraints:

# 1 <= s.length <= 5 * 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.

from typing import List
from collections import defaultdict
import bisect

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        s_indices_map = defaultdict(list)
        for i, ch in enumerate(s):
            s_indices_map[ch].append(i)
        
        count = 0 
        for word in words:
            prev_index = -1   
            for ch in word:
                indices = s_indices_map[ch]
                index = bisect.bisect_right(indices, prev_index)
                if index == len(indices):
                    break
                prev_index = indices[index]
            else:
                count += 1
                
        return count
    
# solution = Solution()
# s = "abcde"
# words = ["a","bb","acd","ace"]
# print(solution.numMatchingSubseq(s, words))