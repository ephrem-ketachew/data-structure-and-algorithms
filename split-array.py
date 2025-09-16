# 2584. Split the Array to Make Coprime Products
# Hard

# You are given a 0-indexed integer array nums of length n.

# A split at an index i where 0 <= i <= n - 2 is called valid if the product of the first i + 1 elements and the product of the remaining elements are coprime.

# For example, if nums = [2, 3, 3], then a split at the index i = 0 is valid because 2 and 9 are coprime, while a split at the index i = 1 is not valid because 6 and 3 are not coprime. A split at the index i = 2 is not valid because i == n - 1.
# Return the smallest index i at which the array can be split validly or -1 if there is no such split.

# Two values val1 and val2 are coprime if gcd(val1, val2) == 1 where gcd(val1, val2) is the greatest common divisor of val1 and val2.

# Example 1:

# Input: nums = [4,7,8,15,3,5]
# Output: 2
# Explanation: The table above shows the values of the product of the first i + 1 elements, the remaining elements, and their gcd at each index i.
# The only valid split is at index 2.
# Example 2:


# Input: nums = [4,7,15,8,3,5]
# Output: -1
# Explanation: The table above shows the values of the product of the first i + 1 elements, the remaining elements, and their gcd at each index i.
# There is no valid split.
 
# Constraints:

# n == nums.length
# 1 <= n <= 104
# 1 <= nums[i] <= 106

from typing import List
from math import gcd, lcm
from collections import Counter

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        # suffix_lcm = [0] * len(nums)
        # right_lcm = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     right_lcm = lcm(right_lcm, nums[i])
        #     suffix_lcm[i] = right_lcm
            
        # left_lcm = right_lcm = 1
        # for i in range(len(nums) - 1):
        #     left_lcm = lcm(left_lcm, nums[i])

        #     if gcd(left_lcm, suffix_lcm[i + 1]) == 1:
        #         return i
            
        # return -1
        
        right_factors = Counter()
        for i in range(len(nums)):
            num = nums[i]
            p = 2
            while num % 2 == 0:
                right_factors[p] += 1
                num /= p
            p = 3
            while p * p <= num:
                while num % p == 0:
                    right_factors[p] += 1
                    num //= p
                p += 2
                
            if num > 1:
                right_factors[num] += 1
                
        left_factors = Counter()  
        # print(right_factors)      
        for i in range(len(nums) - 1):
            num = nums[i]
            p = 2
            while num % 2 == 0:
                left_factors[p] += 1
                right_factors[p] -= 1
                num /= p
            if right_factors[p] == 0:
                del right_factors[p]
            p = 3
            while p * p <= num:
                while num % p == 0:
                    left_factors[p] += 1
                    right_factors[p] -= 1
                    num //= p
                    
                if right_factors[p] == 0:
                    del right_factors[p]
                    
                p += 2
                
            if num > 1:
                left_factors[num] += 1
                right_factors[num] -= 1
                
            if right_factors[num] == 0:
                del right_factors[num]
                
            if not(left_factors.keys() & right_factors.keys()):
                return i
            
            # print(i, left_factors, right_factors)
            
        return -1
    
solution = Solution()
nums = [4,7,8,15,3,5]
nums = [4,7,15,8,3,5]
print(solution.findValidSplit(nums))