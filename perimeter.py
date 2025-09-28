# 976. Largest Perimeter Triangle
# Easy
# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

# Example 1:

# Input: nums = [2,1,2]
# Output: 5
# Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
# Example 2:

# Input: nums = [1,2,1,10]
# Output: 0
# Explanation: 
# You cannot use the side lengths 1, 1, and 2 to form a triangle.
# You cannot use the side lengths 1, 1, and 10 to form a triangle.
# You cannot use the side lengths 1, 2, and 10 to form a triangle.
# As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
 

# Constraints:

# 3 <= nums.length <= 104
# 1 <= nums[i] <= 106

from typing import List
# import bisect

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # largest = 0
        # nums.sort()
        
        # for i in range(len(nums) - 2):
        #     for j in range(i + 1, len(nums) - 1):
        #         s = nums[i] + nums[j]
        #         k = bisect.bisect_left(nums, s)
                
        #         if 0 <= k < len(nums) and k > j and s > nums[k]:
        #             largest = max(largest, s + nums[k])
                    
        #         elif len(nums) > k - 1 > 0 and k - 1 > j and s > nums[k - 1]:
        #             largest = max(largest, s + nums[k - 1])
                
        # return largest
        
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i + 1] + nums[i + 2] > nums[i]:
                return nums[i] + nums[i + 1] + nums[i + 2]
            
        return 0