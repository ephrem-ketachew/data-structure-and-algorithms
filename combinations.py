# 77. Combinations
# Medium

# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

# Example 1:

# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
# Example 2:

# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
 
# Constraints:

# 1 <= n <= 20
# 1 <= k <= n

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # nums = list(range(1, n + 1))
        # res = []
        # def backtrack(index: int, current_subset: list[int]) -> None:
        #     if len(current_subset) == k:
        #         res.append(current_subset[:])
        #         return
            
        #     for i in range(index, len(nums)):
        #         current_subset.append(nums[i])
        #         backtrack(i + 1, current_subset)
        #         current_subset.pop()
                
        # backtrack(0, [])
        # return res
        
        res = []
        def backtrack(index: int, current_subset: list[int]) -> None:
            if len(current_subset) == k:
                res.append(current_subset[:])
                return
            
            for i in range(index, n + 1):
                current_len = len(current_subset)
                remaining_len = n - i + 1
                if current_len + remaining_len < k:
                    break
                
                current_subset.append(i)
                backtrack(i + 1, current_subset)
                current_subset.pop()
                
        backtrack(1, [])
        return res