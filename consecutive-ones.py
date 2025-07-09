# 485. Max Consecutive Ones
# Easy
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        left = None
        for right in range(len(nums)):
            if nums[right] == 1:
                if left is None:
                    left = right
                max_ones = max(max_ones, right - left + 1)
            else:
                left = None
                
        return max_ones