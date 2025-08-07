# 524. Longest Word in Dictionary through Deleting
# Medium
# Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

# Example 1:

# Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# Output: "apple"
# Example 2:

# Input: s = "abpcplea", dictionary = ["a","b","c"]
# Output: "a"

# Constraints:

# 1 <= s.length <= 1000
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 1000
# s and dictionary[i] consist of lowercase English letters.

from typing import List
from collections import defaultdict
from bisect import bisect_right

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # def is_subsequence(s, string):
        #     if len(s) > len(string):
        #         return False
        #     i = j = 0
        #     while i < len(s) and j < len(string):
        #         if string[j] == s[i]:
        #             i += 1
        #         j += 1
        #     return i == len(s)
        
        # dictionary.sort(key=lambda word: (-len(word), word))
   
        # for i, word in enumerate(dictionary):
        #     if i > 0 and word == dictionary[i - 1]:
        #         continue
        #     if is_subsequence(word, s):
        #         return word
        
        # return ''
        
        s_indices_map = defaultdict(list)
        for i, ch in enumerate(s):
            s_indices_map[ch].append(i)
        
        dictionary = list(set(dictionary))
        dictionary.sort(key=lambda word: (-len(word), word)) 
        for word in dictionary:
            prev_index = -1   
            for ch in word:
                indices = s_indices_map[ch]
                index = bisect_right(indices, prev_index)
                if index == len(indices):
                    break
                prev_index = indices[index]
            else:
                return word
                
        return ''
    
# solution = Solution()
# s = "abpcplea"
# dictionary = ["ale","apple","monkey","plea"]
# print(solution.findLongestWord(s, dictionary))