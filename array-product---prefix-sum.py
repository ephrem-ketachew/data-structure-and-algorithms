# 238. Product of Array Except Self
# Medium
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [1] * (len(nums) + 1)
        suffix[-2] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
            
        prefix = 1
        print(suffix)
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = prefix * suffix[i + 1]
            prefix *= nums[i]
            
        return ans