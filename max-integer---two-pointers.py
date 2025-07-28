# 2441. Largest Positive Integer That Exists With Its Negative
# Easy
# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

# Return the positive integer k. If there is no such integer, return -1.

# Example 1:

# Input: nums = [-1,2,-3,3]
# Output: 3
# Explanation: 3 is the only valid k we can find in the array.
# Example 2:

# Input: nums = [-1,10,6,7,-7,1]
# Output: 7
# Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.
# Example 3:

# Input: nums = [-10,8,6,7,-2,-3]
# Output: -1
# Explanation: There is no a single valid k, we return -1.
 

# Constraints:

# 1 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# nums[i] != 0

from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        maxx = -1
        for num in nums:
            if num > maxx and -num in nums_set:
                maxx = num
                
        return maxx
        
        # nums.sort()
        # left, right = 0, len(nums) -1
        # maxx = -1
        # while left < right:
        #     summ = nums[left] + nums[right]
        #     if summ == 0:
        #         maxx = max(maxx, nums[right])
        #         left += 1
        #         right -=1
        #     elif summ < 0:
        #         left += 1
        #     else:
        #         right -= 1
                
        # return maxx
    
# solution = Solution()
# nums = [-1,2,-3,3]
# print(solution.findMaxK(nums))