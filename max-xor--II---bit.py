# 421. Maximum XOR of Two Numbers in an Array
# Medium

# Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

# Example 1:

# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.
# Example 2:

# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127

# Constraints:

# 1 <= nums.length <= 2 * 105
# 0 <= nums[i] <= 231 - 1

from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        mask = 0
        for bit in range(31, -1, -1):
            mask |= 1 << bit
            prefix = set(num & mask for num in nums)
            candidate = ans | 1 << bit
            for p in prefix:
                if p ^ candidate in prefix:
                    ans = candidate
                    break
                
        return ans