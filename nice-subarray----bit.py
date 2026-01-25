# 2401. Longest Nice Subarray
# Medium

# You are given an array nums consisting of positive integers.

# We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

# Return the length of the longest nice subarray.

# A subarray is a contiguous part of an array.

# Note that subarrays of length 1 are always considered nice.

# Example 1:

# Input: nums = [1,3,8,48,10]
# Output: 3
# Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
# - 3 AND 8 = 0.
# - 3 AND 48 = 0.
# - 8 AND 48 = 0.
# It can be proven that no longer nice subarray can be obtained, so we return 3.
# Example 2:

# Input: nums = [3,1,5,11,13]
# Output: 1
# Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.
 
# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109

from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # n, left, max_len = len(nums), 0, 1
        # bit_len = max(nums).bit_length()
        # bits = [0] * bit_len
        # for right in range(n):
        #     for bit in range(bit_len):
        #         if nums[right] & (1 << bit):
        #             bits[bit] += 1
                    
        #             while bits[bit] > 1:
        #                 for b in range(bit_len):
        #                     if nums[left] & (1 << b):
        #                         bits[b] -= 1
        #                 left += 1
                
        #     max_len = max(max_len, right - left + 1)
            
        # return max_len
        
        left = 0
        mask = 0
        max_len = 1
        
        for right in range(len(nums)):
            while mask & nums[right]:
                mask ^= nums[left]
                left += 1
                
            mask |= nums[right]
            
            max_len = max(max_len, right - left + 1)
            
        return max_len