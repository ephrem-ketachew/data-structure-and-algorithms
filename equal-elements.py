# 3488. Closest Equal Element Queries
# Medium

# You are given a circular array nums and an array queries.

# For each query i, you have to find the following:

# The minimum distance between the element at index queries[i] and any other index j in the circular array, where nums[j] == nums[queries[i]]. If no such index exists, the answer for that query should be -1.
# Return an array answer of the same size as queries, where answer[i] represents the result for query i.

# Example 1:

# Input: nums = [1,3,1,4,1,3,2], queries = [0,3,5]

# Output: [2,-1,3]

# Explanation:

# Query 0: The element at queries[0] = 0 is nums[0] = 1. The nearest index with the same value is 2, and the distance between them is 2.
# Query 1: The element at queries[1] = 3 is nums[3] = 4. No other index contains 4, so the result is -1.
# Query 2: The element at queries[2] = 5 is nums[5] = 3. The nearest index with the same value is 1, and the distance between them is 3 (following the circular path: 5 -> 6 -> 0 -> 1).
# Example 2:

# Input: nums = [1,2,3,4], queries = [0,1,2,3]

# Output: [-1,-1,-1,-1]

# Explanation:

# Each value in nums is unique, so no index shares the same value as the queried element. This results in -1 for all queries. 

# Constraints:

# 1 <= queries.length <= nums.length <= 105
# 1 <= nums[i] <= 106
# 0 <= queries[i] < nums.length

from typing import List
from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        num_idx = defaultdict(list)
        for i, num in enumerate(nums):
            num_idx[num].append(i)
            
        ans = [-1] * len(queries)
        for i, idx in enumerate(queries):
            num = nums[idx]
            if len(num_idx[num]) < 2:
                continue
            
            arr = num_idx[num]
            n = len(arr)
            k = bisect.bisect_left(arr, idx)
            min_dist = len(nums) - 1
            if k - 1 >= 0:
                min_dist = min(min_dist, idx - arr[k - 1])
            if k + 1 < n:
                min_dist = min(min_dist, arr[k + 1] - idx)
                
            if k == 0 or k == n - 1:
                min_dist = min(min_dist, arr[0] + len(nums) - arr[-1])
                
            ans[i] = min_dist
                
        return ans