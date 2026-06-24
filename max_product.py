# 152. Maximum Product Subarray
# Medium

# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Note that the product of an array with a single element is the value of that element.

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 
# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = cur_max = global_max = nums[0]
        for i in range(1, len(nums)):
            temp_max = max(nums[i], nums[i] * cur_min, nums[i] * cur_max)
            cur_min = min(nums[i], nums[i] * cur_min, nums[i] * cur_max)
            cur_max = temp_max
            global_max = max(global_max, cur_max)
            
        return global_max