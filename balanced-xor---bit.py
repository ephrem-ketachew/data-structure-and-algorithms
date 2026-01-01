# 3755. Find Maximum Balanced XOR Subarray Length
# Medium

# Given an integer array nums, return the length of the longest subarray that has a bitwise XOR of zero and contains an equal number of even and odd numbers. If no such subarray exists, return 0.

# Example 1:

# Input: nums = [3,1,3,2,0]

# Output: 4

# Explanation:

# The subarray [1, 3, 2, 0] has bitwise XOR 1 XOR 3 XOR 2 XOR 0 = 0 and contains 2 even and 2 odd numbers.

# Example 2:

# Input: nums = [3,2,8,5,4,14,9,15]

# Output: 8

# Explanation:

# The whole array has bitwise XOR 0 and contains 4 even and 4 odd numbers.

# Example 3:

# Input: nums = [0]

# Output: 0

# Explanation:

# No non-empty subarray satisfies both conditions.

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109

from typing import List
from collections import defaultdict

class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        # seen = defaultdict(list)
        # seen[0].append(-1)
        # xor = 0
        # max_len = 0
        # prefix_odds = [0] * (len(nums) + 1)
        # for i in range(len(nums)):
        #     prefix_odds[i + 1] = prefix_odds[i]
        #     if nums[i] % 2:
        #         prefix_odds[i + 1] += 1
           
        # for idx, num in enumerate(nums):
        #     xor ^= num
        #     if xor in seen:
        #         for i in seen[xor]:
        #             prev_idx = i + 1
        #             odds = prefix_odds[idx + 1] - prefix_odds[prev_idx]
        #             evens = idx + 1 - prev_idx - odds
        #             if odds == evens:
        #                 max_len = max(max_len, odds + evens)
            
        #     seen[xor].append(idx)
            
        # return max_len
        
        balance = 0
        xor = 0
        seen = {}
        max_len = 0
        
        seen[(0, 0)] = -1
        
        for i in range(len(nums)):
            xor ^= nums[i]
            if nums[i] % 2:
                balance += 1
            else:
                balance -= 1
                
            state = (xor, balance)
            if state in seen:
                max_len = max(max_len, i - seen[state])
            else:
                seen[state] = i
                
        return max_len