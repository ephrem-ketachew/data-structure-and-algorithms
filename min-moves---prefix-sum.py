# 1674. Minimum Moves to Make Array Complementary
# Medium

# You are given an integer array nums of even length n and an integer limit. In one move, you can replace any integer from nums with another integer between 1 and limit, inclusive.

# The array nums is complementary if for all indices i (0-indexed), nums[i] + nums[n - 1 - i] equals the same number. For example, the array [1,2,3,4] is complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.

# Return the minimum number of moves required to make nums complementary. 

# Example 1:

# Input: nums = [1,2,4,3], limit = 4
# Output: 1
# Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
# nums[0] + nums[3] = 1 + 3 = 4.
# nums[1] + nums[2] = 2 + 2 = 4.
# nums[2] + nums[1] = 2 + 2 = 4.
# nums[3] + nums[0] = 3 + 1 = 4.
# Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.
# Example 2:

# Input: nums = [1,2,2,1], limit = 2
# Output: 2
# Explanation: In 2 moves, you can change nums to [2,2,2,2]. You cannot change any number to 3 since 3 > limit.
# Example 3:

# Input: nums = [1,2,1,2], limit = 2
# Output: 0
# Explanation: nums is already complementary.

# Constraints:

# n == nums.length
# 2 <= n <= 105
# 1 <= nums[i] <= limit <= 105
# n is even.

from typing import List
from collections import Counter

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        delta = [0] * (2 * limit + 2)
        for i in range(n // 2):
            mn = min(nums[i], nums[n - 1 - i])
            mx = max(nums[i], nums[n - 1 - i])
            s = nums[i] + nums[n - 1 - i]
            
            delta[1 + mn] -= 1
            delta[limit + mx + 1] += 1
            
            delta[s] -= 1
            delta[s + 1] += 1
            
        min_move = n
        prefix = n
        for i in range(2, 2 * limit + 1):
            prefix += delta[i]
            min_move = min(min_move, prefix)
            
        return min_move