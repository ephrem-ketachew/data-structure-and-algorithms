# 2444. Count Subarrays With Fixed Bounds
# Hard

# You are given an integer array nums and two integers minK and maxK.

# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.

# A subarray is a contiguous part of an array.

# Example 1:

# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
# Example 2:

# Input: nums = [1,1,1,1], minK = 1, maxK = 1
# Output: 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

# Constraints:

# 2 <= nums.length <= 105
# 1 <= nums[i], minK, maxK <= 106

from typing import List
import heapq
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # def at_most_max_at_least_min(minmum, maximum):
        #     min_heap = []
        #     max_heap = []
        #     min_deleted = defaultdict(int)
        #     max_deleted = defaultdict(int)
        #     count = left = 0
            
        #     def get_max():
        #         while max_heap and max_deleted[-max_heap[0]] > 0:
        #             num = -heapq.heappop(max_heap)
        #             max_deleted[num] -= 1
        #             if max_deleted[num] == 0:
        #                 del max_deleted[num]
        #         return -max_heap[0] if max_heap else 0
                
        #     def get_min():
        #         while min_heap and min_deleted[min_heap[0]] > 0:
        #             num = heapq.heappop(min_heap)
        #             min_deleted[num] -= 1
        #             if min_deleted[num] == 0:
        #                 del min_deleted[num]
        #         return min_heap[0] if min_heap else float('inf')
            
        #     for right in range(len(nums)):
        #         heapq.heappush(min_heap, nums[right])
        #         heapq.heappush(max_heap, -nums[right])
                
        #         while get_max() > maximum:
        #             max_deleted[nums[left]] += 1
        #             min_deleted[nums[left]] += 1
        #             left += 1
                    
        #         while get_min() < minmum:
        #             max_deleted[nums[left]] += 1
        #             min_deleted[nums[left]] += 1
        #             left += 1
                    
        #         count += right - left + 1
                
        #     return count
        
        # return (
        #     at_most_max_at_least_min(minK, maxK) -
        #     at_most_max_at_least_min(minK, maxK - 1) -
        #     at_most_max_at_least_min(minK + 1, maxK) +
        #     at_most_max_at_least_min(minK + 1, maxK - 1)
        # )
        
        
        min_pos = max_pos = left = -1
        count = 0
        
        for right in range(len(nums)):
            if not minK <= nums[right] <= maxK:
                left = right
                
            if nums[right] == minK:
                min_pos = right
                
            if nums[right] == maxK:
                max_pos = right
                
            start = min(min_pos, max_pos)
            
            if left < start:
                count += start - left
                
        return count
    
# solution = Solution()
# nums = [1,3,5,2,7,5]
# minK = 1
# maxK = 5
# nums = [1,1,1,1]
# minK = 1
# maxK = 1
# print(solution.countSubarrays(nums, minK, maxK))