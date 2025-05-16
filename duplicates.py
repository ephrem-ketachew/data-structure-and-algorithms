# 442. Find All Duplicates in an Array
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output
# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # seen = {}
        # duplicates = []
        # for num in nums:
        #     if num in seen:
        #         duplicates.append(num)
        #     else:
        #         seen[num] = True
        # return duplicates
        
        duplicates = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicates.append(abs(num))
            else:
                nums[index] = -nums[index]
                
        return duplicates