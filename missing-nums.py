# 448. Find All Numbers Disappeared in an Array
# Easy

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 
# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n

# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # missing_nums = []
        # nums_set = set(nums)
        # for i in range(1, len(nums) + 1):
        #     if i not in nums_set:
        #         missing_nums.append(i)
                
        # return missing_nums
        
        missing_nums = []
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
                
        for i in range(n):
            if nums[i] != i + 1:
                missing_nums.append(i + 1)
                
        return missing_nums               