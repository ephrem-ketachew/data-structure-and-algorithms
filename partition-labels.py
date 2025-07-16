# 763. Partition Labels
# Medium
# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10]
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {char:i for i, char in enumerate(s)}
        start, end = 0, 0
        ans = []
        
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if end == i:
                ans.append(end - start + 1)
                start = i + 1
                
        return ans
        
        # seen, ans = [], []
    
        # for i, num in enumerate(s):
        #     for j, sub in enumerate(seen):
        #         if num in sub[0]:
        #             index = sub[1]
        #             s1 = set(s[index:i + 1])
        #             sub[0] = s1
        #             sub[2] = i
        #             while len(seen) > j + 1:
        #                 seen.pop()
        #             break
        #     else:
        #         sub = set([num])
        #         seen.append([sub, i, i])
            
        # for sub in seen:
        #     ans.append(sub[2] - sub[1] + 1)
            
        # return ans
                
# solution = Solution()
# s = "ababcbacadefegdehijhklij"
# print(solution.partitionLabels(s))