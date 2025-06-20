# 1752. Check if Array Is Sorted and Rotated

# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 3 positions to begin on the element of value 3: [3,4,5,1,2].
# Example 2:

# Input: nums = [2,1,3,4]
# Output: false
# Explanation: There is no sorted array once rotated that can make nums.
# Example 3:

# Input: nums = [1,2,3]
# Output: true
# Explanation: [1,2,3] is the original sorted array.
# You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] > nums[(i + 1) % len(nums)]:
        #         count += 1
        #         if count > 1:
        #             return False
        # return True
        
        sorted_nums = nums.copy()
        sorted_nums.sort()
        
        if sorted_nums == nums:
            return True
        
        if nums[0] not in sorted_nums[1:]:
            return False
       
        j = index = sorted_nums.index(nums[0], 1)
        k = (len(nums) - index) % len(nums)
        while j < len(sorted_nums) and sorted_nums[j] == sorted_nums[index]:
            rotated_array = [0] * len(sorted_nums)
            are_same = True
            for i in range(len(sorted_nums)):
                rotated_array[i] = sorted_nums[i - k]
                if rotated_array[i] != nums[i]:
                    are_same = False
                    break
            print(rotated_array)
            if are_same:
                return True
            j += 1
            k = len(nums) - j
        return False