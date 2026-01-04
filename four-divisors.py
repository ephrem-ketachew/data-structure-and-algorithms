# 1390. Four Divisors
# Medium

# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

# Example 1:

# Input: nums = [21,4,7]
# Output: 32
# Explanation: 
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.
# Example 2:

# Input: nums = [21,21]
# Output: 64
# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 0

# Constraints:

# 1 <= nums.length <= 104
# 1 <= nums[i] <= 105

from typing import List
from math import sqrt

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            factors_count = 0
            factors_sum = 0
            for i in range(1, int(sqrt(num) + 1)):
                if num % i == 0:
                    factors_count += 2
                    factors_sum += i + num // i
                    if i * i == num:
                        factors_count -= 1
                        factors_sum -= 1
                if factors_count > 4:
                    break
            if factors_count == 4:
                total += factors_sum
                
        return total