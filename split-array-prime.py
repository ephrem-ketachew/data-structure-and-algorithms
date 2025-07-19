# Q1. Split Array by Prime Indices
# Medium
# 4 pt.
# You are given an integer array nums.

# Split nums into two arrays A and B using the following rule:

# Elements at prime indices in nums must go into array A.
# All other elements must go into array B.
# Return the absolute difference between the sums of the two arrays: |sum(A) - sum(B)|.

# A prime number is a natural number greater than 1 with only two factors, 1 and itself.

# Note: An empty array has a sum of 0.

# Example 1:

# Input: nums = [2,3,4]

# Output: 1

# Explanation:

# The only prime index in the array is 2, so nums[2] = 4 is placed in array A.
# The remaining elements, nums[0] = 2 and nums[1] = 3 are placed in array B.
# sum(A) = 4, sum(B) = 2 + 3 = 5.
# The absolute difference is |4 - 5| = 1.
# Example 2:

# Input: nums = [-1,5,7,0]

# Output: 3

# Explanation:

# The prime indices in the array are 2 and 3, so nums[2] = 7 and nums[3] = 0 are placed in array A.
# The remaining elements, nums[0] = -1 and nums[1] = 5 are placed in array B.
# sum(A) = 7 + 0 = 7, sum(B) = -1 + 5 = 4.
# The absolute difference is |7 - 4| = 3.

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 

from typing import List

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        def is_prime(n):
            if n < 2:
                return False
            
            if n == 2 or n == 3:
                return True
            
            if n % 2 == 0 or n % 3 == 0:
                return False
            
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
                
            return True
        
        a = 0
        b = 0
        
        for i in range(len(nums)):
            if is_prime(i):
                a += nums[i]
            else:
                b += nums[i]
                
        return abs(a - b)
    
# solution = Solution()
# nums = [2,3,4]
# nums = [-1,5,7,0]
# print(solution.splitArray(nums))