# 413. Arithmetic Slices
# Medium
# An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.

# A subarray is a contiguous subsequence of the array.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: 3
# Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
# Example 2:

# Input: nums = [1]
# Output: 0

# Constraints:

# 1 <= nums.length <= 5000
# -1000 <= nums[i] <= 1000

from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        count = 0
        left = 0
        diff = nums[1] - nums[0]
        
        for right in range(2, len(nums)):
            if nums[right] - nums[right - 1] == diff:
                count += (right - left + 1) - 3 + 1
            else:
                left = right - 1
                diff = nums[right] - nums[left]
                
        return count
    
# solution = Solution()
# nums = [1,2,3,4]
# print(solution.numberOfArithmeticSlices(nums))