# 581. Shortest Unsorted Continuous Subarray
# Medium
# Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

# Return the shortest such subarray and output its length.

# Example 1:

# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 0
# Example 3:

# Input: nums = [1]
# Output: 0
 
# Constraints:

# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105

# Follow up: Can you solve it in O(n) time complexity?

from typing import List
from bisect import bisect_right

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # APPROACH #1 : COMPLEX, LESS EFFICIENT(TECHNICALLY O(NLOG(N))), EDGE CASE HELL YET IN PLACE AND ONE PASS
        # left = right = float('inf')
        # maxx = nums[0]
        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i - 1]:
        #         left = min(left, bisect_right(nums, nums[i], hi=i - 1))
        #         right = i
                
        #     if nums[i] < maxx:
        #         right = i
        #     maxx = max(maxx, nums[i])
                    
        # return right - left + 1 if left != float('inf') else 0
        
        # APPROACH #2 : SIMPLE, MORE EFFICIENT(YET STILL O(NLOG(N))) BUT ADDITIONAL O(N) SPACE 
        # left = right = -1
        # sorted_nums = nums[:]
        # sorted_nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] != sorted_nums[i]:
        #         if left == -1:
        #             left = i
        #         right = i
                    
        # return right - left + 1 if left != -1 else 0
        
        # APPROACH #3 : SIMPLE, MOST EFFICIENT(O(N) TIME AND O(1) SPACE COMPLEXITY)
        left, right = -1, -2
        
        max_seen = nums[0]
        for i in range(1, len(nums)):
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                right = i
                
        min_seen = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            min_seen = min(min_seen, nums[i])
            if nums[i] > min_seen:
                left = i
                
        return right - left + 1
           
# solution = Solution()
# nums = [2,6,4,8,10,9,15]
# nums = [1,2,3,4]
# nums = [2,3,3,2,4]
# nums = [1,2,4,5,3]
# nums = [1,3,5,2,4]
# print(solution.findUnsortedSubarray(nums))