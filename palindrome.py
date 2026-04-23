# 131. Palindrome Partitioning
# Medium

# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]

# Constraints:

# 1 <= s.length <= 16
# s contains only lowercase English letters.

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)
        def backtrack(index: int, currrent_partition: List[str]):
            if index == n:
                ans.append(currrent_partition[:])
                return
                
            for i in range(index, n):
                current_slice = s[index: i + 1]
                if current_slice == current_slice[::-1]:
                    currrent_partition.append(current_slice)
                    backtrack(i + 1, currrent_partition)
                    currrent_partition.pop()
                
        backtrack(0, [])
        return ans