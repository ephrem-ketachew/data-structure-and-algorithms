# 336. Palindrome Pairs
# Hard
# You are given a 0-indexed array of unique strings words.

# A palindrome pair is a pair of integers (i, j) such that:

# 0 <= i, j < words.length,
# i != j, and
# words[i] + words[j] (the concatenation of the two strings) is a palindrome.
# Return an array of all the palindrome pairs of words.

# You must write an algorithm with O(sum of words[i].length) runtime complexity.

# Example 1:

# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
# Example 2:

# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
# Example 3:

# Input: words = ["a",""]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["a","a"]

# Constraints:

# 1 <= words.length <= 5000
# 0 <= words[i].length <= 300
# words[i] consists of lowercase English letters.

from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_map = {word:i for i, word in enumerate(words)}
        
        ans = []
        for i, word in enumerate(words):
            for k in range(len(word) + 1):
                prefix = word[:k]
                suffix = word[k:]
                
                if prefix == prefix[::-1]:
                    suffix_rev = suffix[::-1]
                    if suffix_rev in word_map and word_map[suffix_rev] != i:
                        ans.append([word_map[suffix_rev], i])
                        
                if suffix == suffix[::-1]:
                    prefix_rev = prefix[::-1]
                    if k != len(word) and prefix_rev in word_map and word_map[prefix_rev] != i:
                        ans.append([i, word_map[prefix_rev]])
                        
        return ans