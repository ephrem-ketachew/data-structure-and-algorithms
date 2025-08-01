# 922. Sort Array By Parity II
# Easy
# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

# Return any answer array that satisfies this condition.

# Example 1:

# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
# Example 2:

# Input: nums = [2,3]
# Output: [2,3]

# Constraints:

# 2 <= nums.length <= 2 * 104
# nums.length is even.
# Half of the integers in nums are even.
# 0 <= nums[i] <= 1000

# Follow Up: Could you solve it in-place?

from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # odds = []
        # evens = []
        
        # for num in nums:
        #     evens.append(num) if num % 2 == 0 else odds.append(num)
        
        # j = k = 0    
        # for i in range(len(nums)):
        #     if i % 2 == 0:
        #         nums[i] = evens[j]
        #         j += 1
        #     else:
        #         nums[i] = odds[k]
        #         k += 1
                
        # return nums
        
        # j = k = 0
        # for i in range(len(nums)):
        #     while j < len(nums) and nums[j] % 2 != 0:
        #         j += 1
        #     while k < len(nums) and nums[k] % 2 != 1:
        #         k += 1
                
        #     if i % 2 == 0:
        #         if i == j:
        #             j += 1
        #         else:
        #             nums[i], nums[j] = nums[j], nums[i]
        #     else:
        #         if i == k:
        #             k += 1
        #         else:
        #             nums[i], nums[k] = nums[k], nums[i]
                    
        # return nums
        
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[j], nums[i] = nums[i], nums[j]
                i += 2
                j += 2
                
        return nums            