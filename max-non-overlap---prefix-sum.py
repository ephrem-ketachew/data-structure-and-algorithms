# 1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
# Medium

# Given an array nums and an integer target, return the maximum number of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to target.

# Example 1:

# Input: nums = [1,1,1,1,1], target = 2
# Output: 2
# Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals to target(2).
# Example 2:

# Input: nums = [-1,3,5,1,4,2,-9], target = 6
# Output: 2
# Explanation: There are 3 subarrays with sum equal to 6.
# ([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 0 <= target <= 106

from typing import List
from collections import defaultdict

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0
        seen = {0}
        prefix = 0
        for i in range(n):
            prefix += nums[i]
            if prefix - target in seen:
                seen = {0}
                count += 1
                prefix = 0
            else:
                seen.add(prefix)
                
        return count
        