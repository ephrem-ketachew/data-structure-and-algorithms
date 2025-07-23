# 3467. Transform Array by Parity
# Easy
# You are given an integer array nums. Transform nums by performing the following operations in the exact order specified:

# Replace each even number with 0.
# Replace each odd numbers with 1.
# Sort the modified array in non-decreasing order.
# Return the resulting array after performing these operations.

# Example 1:

# Input: nums = [4,3,2,1]

# Output: [0,0,1,1]

# Explanation:

# Replace the even numbers (4 and 2) with 0 and the odd numbers (3 and 1) with 1. Now, nums = [0, 1, 0, 1].
# After sorting nums in non-descending order, nums = [0, 0, 1, 1].
# Example 2:

# Input: nums = [1,5,1,4,2]

# Output: [0,0,1,1,1]

# Explanation:

# Replace the even numbers (4 and 2) with 0 and the odd numbers (1, 5 and 1) with 1. Now, nums = [1, 1, 1, 0, 0].
# After sorting nums in non-descending order, nums = [0, 0, 1, 1, 1].

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 1000

from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        # return sorted(0 if num % 2 == 0 else 1 for num in nums)
    
        left = 0
        right = len(nums) - 1
        i = 0
        while i < len(nums):
            if nums[i] % 2 == 0:
                nums[left] = 0
                left += 1
            else:
                nums[i] = nums[right]
                nums[right] = 1
                right -= 1
                i -= 1
                
            if right < left:
                break
            
            i += 1
            
        return nums