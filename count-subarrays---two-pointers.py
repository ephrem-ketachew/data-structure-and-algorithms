# 795. Number of Subarrays with Bounded Maximum
# Medium
# Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example 1:

# Input: nums = [2,1,4,3], left = 2, right = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
# Example 2:

# Input: nums = [2,9,2,5,6], left = 2, right = 8
# Output: 7
 
# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= left <= right <= 109

from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # start, end = -1, -2
        # count = 0
        # for i in range(len(nums)):  
        #     if nums[i] > right:
        #         start, end = -1, -2 # so that count becomes 0
            
        #     if nums[i] <= right and start == -1:
        #         start, end = i, i - 1 # so that count becomes 0
                
        #     if left <= nums[i] <= right:
        #         end = i
                
        #     count += end - start + 1
                
        # return count
        
        def __numSubarrayBoundedMax(bound: int):
            res = cur = 0
            for num in nums:
                if num <= bound:
                    cur += 1
                else:
                    cur = 0
                res += cur
                
            return res
        
        return __numSubarrayBoundedMax(right) - __numSubarrayBoundedMax(left - 1)
    
# solution = Solution()
# nums = [2,1,4,3]
# left = 2
# right = 3
# nums = [2,9,2,5,6]
# left = 2
# right = 8
# print(solution.numSubarrayBoundedMax(nums, left, right))