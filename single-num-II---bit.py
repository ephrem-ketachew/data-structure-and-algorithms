# 137. Single Number II
# Medium

# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:

# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:

# Input: nums = [0,1,0,1,0,1,99]
# Output: 99

# Constraints:

# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each element in nums appears exactly three times except for one element which appears once.

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mask = 0
        for i in range(32):
            set_bits = 0
            for num in nums:
                if num & (1 << i):
                    set_bits +=  1
            mask |= (set_bits % 3) << i
            
        if mask >= 1 << 31:
            mask -= 1 << 32
            
        return mask