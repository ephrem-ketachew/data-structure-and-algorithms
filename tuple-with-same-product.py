# 1726. Tuple with Same Product

# Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

# Example 1:

# Input: nums = [2,3,4,6]
# Output: 8
# Explanation: There are 8 valid tuples:
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
# Example 2:

# Input: nums = [1,2,4,5,10]
# Output: 16
# Explanation: There are 16 valid tuples:
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 

# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 104
# All elements in nums are distinct.

from typing import List
from collections import Counter
from math import comb

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                product.append(nums[i] * nums[j])
        
        freq = Counter(product).values()
        count = 0
        
        for num in freq:
            if num != 1:
                count += comb(num, 2) * 8
        return count
    
        # nums.sort()
        # count = 0
        # for i in range(len(nums) - 3):
        #     for j in range(i + 1, len(nums) - 2):
        #         for k in range(j + 1, len(nums) - 1):
        #             for l in range(k + 1, len(nums)):
        #                 if nums[i] * nums[l] == nums[j] * nums[k]:
        #                     count += 8
                            
        # return count
    
# nums = [2,3,4,6]
# nums = [1, 2, 3, 4, 6, 12]
# s = Solution()
# print(s.tupleSameProduct(nums))