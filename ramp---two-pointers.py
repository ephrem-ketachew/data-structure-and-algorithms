# 962. Maximum Width Ramp
# Medium
# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

# Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

# Example 1:

# Input: nums = [6,0,8,2,1,5]
# Output: 4
# Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
# Example 2:

# Input: nums = [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 
# Constraints:

# 2 <= nums.length <= 5 * 104
# 0 <= nums[i] <= 5 * 104

from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        
        stack = []
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
                
        max_len = 0
        for i in range(n - 1, -1, -1):
            j = i
            while stack and nums[stack[-1]] <= nums[i]:
                j = stack.pop()
            max_len = max(max_len, i - j)
                
        return max_len    
    
    
        # MY BRUTE FORCE FAILURE 
        # for i in range(n):
        #     if nums[i] < nums[min_index]:
        #         min_index = i
        #         continue
            
        #     right = i - max_len
        #     if nums[i] == nums[min_index]:
        #         right = min(min_index + 1, i - max_len)
                
        #     for j in range(right):
        #         if nums[j] <= nums[i]:
        #             max_len = i - j
        #             break
                
        # return max_len
    
# solution = Solution()
# nums = [6,0,8,2,1,5]
# nums = [9,8,1,0,1,9,4,0,4,1]
# nums = [6,7,8,8,6,5,5,8,2,2]
# print(solution.maxWidthRamp(nums))
                