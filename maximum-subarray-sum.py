# 53. Maximum Subarray

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

import heapq
from typing import List
 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        max_sum = float('-inf')
        heap = [0]
        
        for num in nums:
            prefix += num
            max_sum = max(max_sum, prefix - heap[0])
            heapq.heappush(heap, prefix)
        return max_sum