# 219. Contains Duplicate II
# Easy
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

from typing import List
from collections import Counter

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # first solution
        # window_counter = Counter(nums[:k + 1])
        # if k >= len(nums):
        #     return True if len(window_counter) < len(nums) else False

        # if len(window_counter) < k + 1:
        #         return True
        
        # for i in range(k + 1, len(nums)):
        #     window_counter[nums[i]] += 1
        #     window_counter[nums[i - k - 1]] -= 1
        #     if window_counter[nums[i - k - 1]] == 0:
        #         del window_counter[nums[i - k - 1]]
        #     if len(window_counter) < k + 1:
        #         return True
            
        # return False
        
        # more efficient, readable and simple
        window = set()
        
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if i >= k:
                window.remove(nums[i - k])
                
        return False