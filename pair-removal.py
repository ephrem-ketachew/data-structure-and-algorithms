# 3507. Minimum Pair Removal to Sort Array I
# Easy

# Given an array nums, you can perform the following operation any number of times:

# Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
# Replace the pair with their sum.
# Return the minimum number of operations needed to make the array non-decreasing.

# An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

# Example 1:

# Input: nums = [5,2,3,1]

# Output: 2

# Explanation:

# The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
# The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
# The array nums became non-decreasing in two operations.

# Example 2:

# Input: nums = [1,2,2]

# Output: 0

# Explanation:

# The array nums is already sorted.

# Constraints:

# 1 <= nums.length <= 50
# -1000 <= nums[i] <= 1000

from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted(nums):
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    return False
            return True
        
        def find_min_pair(nums):
            if len(nums) < 2:
                return -1
            a, b = 0, 1
            for i in range(2, len(nums)):
                if nums[i - 1] + nums[i] < nums[a] + nums[b]:
                    a, b = i - 1, i
            return a, b
        
        count = 0
        while not is_sorted(nums):
            a, b = find_min_pair(nums)
            nums[a] = nums[a] + nums[b]
            for i in range(b, len(nums) - 1):
                nums[i] = nums[i + 1]
            nums.pop()
            count += 1
            
        return count