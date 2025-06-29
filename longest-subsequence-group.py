# 2900. Longest Unequal Adjacent Groups Subsequence I
# Easy
# You are given a string array words and a binary array groups both of length n.

# A subsequence of words is alternating if for any two consecutive strings in the sequence, their corresponding elements at the same indices in groups are different (that is, there cannot be consecutive 0 or 1).

# Your task is to select the longest alternating subsequence from words.

# Return the selected subsequence. If there are multiple answers, return any of them.

# Note: The elements in words are distinct. 

# Example 1:

# Input: words = ["e","a","b"], groups = [0,0,1]

# Output: ["e","b"]

# Explanation: A subsequence that can be selected is ["e","b"] because groups[0] != groups[2]. Another subsequence that can be selected is ["a","b"] because groups[1] != groups[2]. It can be demonstrated that the length of the longest subsequence of indices that satisfies the condition is 2.

# Example 2:

# Input: words = ["a","b","c","d"], groups = [1,0,1,1]

# Output: ["a","b","c"]

# Explanation: A subsequence that can be selected is ["a","b","c"] because groups[0] != groups[1] and groups[1] != groups[2]. Another subsequence that can be selected is ["a","b","d"] because groups[0] != groups[1] and groups[1] != groups[3]. It can be shown that the length of the longest subsequence of indices that satisfies the condition is 3. 

# Constraints:

# 1 <= n == words.length == groups.length <= 100
# 1 <= words[i].length <= 10
# groups[i] is either 0 or 1.
# words consists of distinct strings.
# words[i] consists of lowercase English letters.

from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # dp = [[word] for word in words]
        # max_seq = dp[0]
        # for i in range(len(groups)):
        #     if groups[i] == 0:
        #         for j in range(i - 1, -1, -1):
        #             if groups[j] == 1:
        #                 dp[i] = dp[j] + [words[i]]
        #                 if len(dp[i]) > len(max_seq):
        #                     max_seq = dp[i]
        #                 break
        #     else:
        #         for j in range(i - 1, -1, -1):
        #             if groups[j] == 0:
        #                 dp[i] = dp[j] + [words[i]]
        #                 if len(dp[i]) > len(max_seq):
        #                     max_seq = dp[i]
        #                 break
   
        # return max_seq
        
        res = [words[0]]
        prev = groups[0]
        
        for i in range(1, len(words)):
            if groups[i] != prev:
                res.append(words[i])
                prev = groups[i]
                
        return res
        
# solution = Solution()
# words = ["e","a","b"]
# groups = [0,0,1]
# words = ["a","b","c","d"]
# groups = [1,0,1,1]
# print(solution.getLongestSubsequence(words, groups))