# Q2. Longest Common Prefix Between Adjacent Strings After Removals
# Medium
# You are given an array of strings words. For each index i in the range [0, words.length - 1], perform the following steps:

# Remove the element at index i from the words array.
# Compute the length of the longest common prefix among all adjacent pairs in the modified array.
# Return an array answer, where answer[i] is the length of the longest common prefix between the adjacent pairs after removing the element at index i. If no adjacent pairs remain or if none share a common prefix, then answer[i] should be 0.

# A prefix of a string is a substring that starts from the beginning of the string and extends to any point within it.
 

# Example 1:

# Input: words = ["jump","run","run","jump","run"]

# Output: [3,0,0,3,3]

# Explanation:

# Removing index 0:
# words becomes ["run", "run", "jump", "run"]
# Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
# Removing index 1:
# words becomes ["jump", "run", "jump", "run"]
# No adjacent pairs share a common prefix (length 0)
# Removing index 2:
# words becomes ["jump", "run", "jump", "run"]
# No adjacent pairs share a common prefix (length 0)
# Removing index 3:
# words becomes ["jump", "run", "run", "run"]
# Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
# Removing index 4:
# words becomes ["jump", "run", "run", "jump"]
# Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
# Example 2:

# Input: words = ["dog","racer","car"]

# Output: [0,0,0]

# Explanation:

# Removing any index results in an answer of 0.
 

# Constraints:

# 1 <= words.length <= 105
# 1 <= words[i].length <= 104
# words[i] consists of lowercase English letters.
# The sum of words[i].length is smaller than or equal 105.
from typing import List

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        answer = (len(words)) * [0]
        
        if len(words) == 1:
            return [0]
        
        def lcp(word1, word2):
            l = 0
            for i in range(len(word1)):
                if i < len(word2) and word1[i] == word2[i]:
                    l += 1
                else:
                    break
            return l
        
        adj_len = [lcp(words[i], words[i + 1]) for i in range(len(words) - 1)]
        
        max_prefix_len = [0] * len(adj_len)
        max_suffix_len = [0] * len(adj_len)
        
        max_prefix_len[0] = adj_len[0]
        for i in range(1, len(adj_len)):
            max_prefix_len[i] = max(max_prefix_len[i - 1], adj_len[i])
            
        max_suffix_len[-1] = adj_len[-1]
        for i in range(len(adj_len) - 2, -1, -1):
            max_suffix_len[i] = max(max_suffix_len[i + 1], adj_len[i])
        
        for i in range(len(words)):
            if i == 0:
                max_lcp = max_suffix_len[i + 1] if i + 2 < len(words) else 0
            elif i == len(words) - 1:
                if i - 2 >= 0:
                    max_lcp = max_prefix_len[i - 2]
                else:
                    max_lcp = 0
            else:
                new_lcp = lcp(words[i - 1], words[i + 1])
                prefix = max_prefix_len[i - 2] if i - 2 >= 0 else 0
                suffix = max_suffix_len[i + 1] if i + 2 < len(words) else 0
                max_lcp = max(new_lcp, prefix, suffix)
            answer[i] = max_lcp
            
        return answer
            
        # my first solution
        # answer = []     
        # for i in range(len(words)):
        #     max_length = 0
        #     for j in range(len(words) - 1):
        #         if j == i:
        #             continue
        #         length = 0
        #         index_add = 1
        #         if j + 1 == i:
        #             if i == len(words) - 1:
        #                 continue
        #             index_add = 2
        #         for k in range(len(words[j])):
        #             if k < len(words[j + index_add]) and words[j][k] == words[j + index_add][k]:
        #                 length += 1
        #             else:
        #                 break
        #         max_length = max(max_length, length)
        #     answer.append(max_length)
        
        
        # solution 2 better than 1 but still tle
        # answer = [] 
        # prefix_lens = []
        # for i in range(len(words) - 1):
        #     length = length2 = 0
        #     for j in range(len(words[i])):
        #         if j < len(words[i + 1]) and words[i][j] == words[i + 1][j]:
        #             length += 1
        #         else:
        #             break
        #     if i < len(words) - 2:
        #         for j in range(len(words[i])):
        #             if j < len(words[i + 2]) and words[i][j] == words[i + 2][j]:
        #                 length2 += 1
        #             else:
        #                 break
        #     prefix_lens.append((length, length2, max(length, length2)))
  
        # for i in range(len(words)):
        #     max_len = 0
        #     for j in range(len(words) - 1):
        #         if i == j:
        #             l = 0
        #         elif j == i - 1:
        #             l = prefix_lens[j][1]
        #         else:
        #             l = prefix_lens[j][0]
        #         max_len = max(max_len, l)
        #     answer.append(max_len)
        # return answer
    
# solution = Solution()
# words = ["jump","run","run","jump","run"]
# words = ["dog","racer","car"]
# words = ["beeac","aff"]
# print(solution.longestCommonPrefix(words))