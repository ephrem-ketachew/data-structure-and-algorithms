# 334. Increasing Triplet Subsequence
# Medium

# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.

# Constraints:

# 1 <= nums.length <= 5 * 105
# -231 <= nums[i] <= 231 - 1

# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # WRONG APPROACH(FIRST TRIAL) - AINT WE GONNA USE STACK HERE 
        # stack = []
        # nxt_gt = [-1] * len(nums)
        # for i, num in enumerate(nums):
        #     while stack and num > nums[stack[-1]]:
        #         idx = stack.pop()
        #         nxt_gt[idx] = i
        #     stack.append(i)
            
        # for i in range(len(nums)):
        #     if nxt_gt[i] != -1 and nxt_gt[nxt_gt[i]] != -1:
        #         return True
            
        # return False
        
        # ANOTHER APPROACH(SECOND TRIAL) - PREFIX SUM   
        suffix_max = [0] * len(nums)
        suffix_max[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix_max[i] = max(nums[i], suffix_max[i + 1])
        
        min_seen = nums[0]
        for i in range(1, len(nums) - 1):
            if min_seen < nums[i] < suffix_max[i + 1]:
                return True
            min_seen = min(min_seen, nums[i])
            
        return False