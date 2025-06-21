# Q1. Minimum Adjacent Swaps to Alternate Parity
# Medium
# 4 pt.
# You are given an array nums of distinct integers.

# In one operation, you can swap any two adjacent elements in the array.

# An arrangement of the array is considered valid if the parity of adjacent elements alternates, meaning every pair of neighboring elements consists of one even and one odd number.

# Return the minimum number of adjacent swaps required to transform nums into any valid arrangement.

# If it is impossible to rearrange nums such that no two adjacent elements have the same parity, return -1.

 

# Example 1:

# Input: nums = [2,4,6,5,7]

# Output: 3

# Explanation:

# Swapping 5 and 6, the array becomes [2,4,5,6,7]

# Swapping 5 and 4, the array becomes [2,5,4,6,7]

# Swapping 6 and 7, the array becomes [2,5,4,7,6]. The array is now a valid arrangement. Thus, the answer is 3.

# Example 2:

# Input: nums = [2,4,5,7]

# Output: 1

# Explanation:

# By swapping 4 and 5, the array becomes [2,5,4,7], which is a valid arrangement. Thus, the answer is 1.

# Example 3:

# Input: nums = [1,2,3]

# Output: 0

# Explanation:

# The array is already a valid arrangement. Thus, no operations are needed.

# Example 4:

# Input: nums = [4,5,6,8]

# Output: -1

# Explanation:

# No valid arrangement is possible. Thus, the answer is -1.

 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# All elements in nums are distinct.
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        even_indices = [index for index, num in enumerate(nums) if num % 2 == 0]
        odd_indices = [index for index, num in enumerate(nums) if num % 2]
        
        if abs(len(even_indices) - len(odd_indices)) > 1: return -1
        
        def __minSwap(start_with_even: bool) -> int:
            target_indices = range(0, len(nums), 2)
            swap_count = 0
            
            if start_with_even:
                swap_count = sum(abs(t - e) for e, t in zip(even_indices, target_indices))
            else:
                swap_count = sum(abs(t - o) for o, t in zip(odd_indices, target_indices))
            
            return swap_count
        
        if(len(even_indices) > len(odd_indices)):
            return __minSwap(True)
        elif(len(even_indices) < len(odd_indices)):
            return __minSwap(False)
        else:
            return min(__minSwap(True), __minSwap(False))
        
        # my first Solution ... wasted 90 mins on this approach but it turns out my approach was wrong but yeah good effort.... but i come out of the leetcode biweekly contest with 0 questions solved🥺😅
        # odd = even = 0
        # for i in range(len(nums)):
        #     if nums[i] % 2 == 0:
        #         even += 1
        #     else:
        #         odd += 1
        # if abs(even - odd) > 1:
        #     return -1
        
        # if len(nums) == 1:
        #     return 0
        
        # swap_count = 0
        # if even > odd:
        #     if nums[0] % 2 != 0:
        #         for i in range(1, len(nums)):
        #             if nums[i] % 2 == 0:
        #                 while i > 0:
        #                     nums[i - 1], nums[i] = nums[i], nums[i - 1]
        #                     swap_count += 1
        #                     i -= 1
        #                 break
        # elif odd > even:
        #     if nums[0] % 2 == 0:
        #         for i in range(1, len(nums)):
        #             if nums[i] % 2 != 0:
        #                 while i > 0:
        #                     nums[i - 1], nums[i] = nums[i], nums[i - 1]
        #                     swap_count += 1
        #                     i -= 1
        #                 break
        
        # for i in range(1, len(nums)):
        #     if nums[i - 1] % 2 == nums[i] % 2:
        #         for j in range(i + 1, len(nums)):
        #             if nums[i] % 2 != nums[j] % 2:
        #                 while j > i:
        #                     nums[j - 1], nums[j] = nums[j], nums[j - 1]
        #                     swap_count += 1
        #                     j -= 1
        #                 break
        # return swap_count
        