# 260. Single Number III
# Medium

# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

# Example 1:

# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
# Example 2:

# Input: nums = [-1,0]
# Output: [-1,0]
# Example 3:

# Input: nums = [0,1]
# Output: [1,0]

# Constraints:

# 2 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each integer in nums will appear twice, only two integers will appear once.

from typing import List
from operator import xor
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums_xor = reduce(xor, nums)
        k = 0
        while not (nums_xor & (1 << k)):
            k += 1
            
        first_bin_xor = 0
        second_bin_xor = 0
        for num in nums:
            if num & (1 << k):
                first_bin_xor ^= num
            else:
                second_bin_xor ^= num
                
        return [first_bin_xor, second_bin_xor]