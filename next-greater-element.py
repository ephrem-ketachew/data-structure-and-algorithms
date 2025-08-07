# 503. Next Greater Element II
# Medium

# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

# Example 1:

# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also 2.
# Example 2:

# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]

# Constraints:

# 1 <= nums.length <= 104
# -109 <= nums[i] <= 109

from typing import List
from bisect import bisect_right

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:        
        ans = [-1] * len(nums)
        
        # for i, num in enumerate(nums):
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] > num:
        #             ans[i] = nums[j]
        #             break
        #     else:
        #         for j in range(i):
        #             if nums[j] > num:
        #                 ans[i] = nums[j]
        #                 break
                    
        # return ans
        
        stack = []
        n = len(nums)
        for i in range(2 * n - 1, -1, -1):
            i = i % n
            
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
                
            if stack:
                ans[i] = nums[stack[-1]]
                
            stack.append(i)
                
        return ans
# solution = Solution()
# nums = [1,2,3,4,3]
# print(solution.nextGreaterElements(nums))