# 3584. Maximum Product of First and Last Elements of a Subsequence
# Medium
# You are given an integer array nums and an integer m.

# Return the maximum product of the first and last elements of any subsequence of nums of size m.

# Example 1:

# Input: nums = [-1,-9,2,3,-2,-3,1], m = 1

# Output: 81

# Explanation:

# The subsequence [-9] has the largest product of the first and last elements: -9 * -9 = 81. Therefore, the answer is 81.

# Example 2:

# Input: nums = [1,3,-5,5,6,-4], m = 3

# Output: 20

# Explanation:

# The subsequence [-5, 6, -4] has the largest product of the first and last elements.

# Example 3:

# Input: nums = [2,-1,2,-6,5,2,-5,7], m = 2

# Output: 35

# Explanation:

# The subsequence [5, 7] has the largest product of the first and last elements.

# Constraints:

# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105
# 1 <= m <= nums.length

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:         
        suffix = [(0, 0)] * len(nums)   
        minn, maxx = float('inf'), float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            minn = min(minn, nums[i])
            maxx = max(maxx, nums[i])
            
            suffix[i] = (minn, maxx)
            
        max_product = float('-inf')
        minn, maxx = float('inf'), float('-inf')
        for i in range(len(nums) - m + 1):
            minn = min(minn, nums[i])
            maxx = max(maxx, nums[i])
            
            max_product = max(max_product, minn * suffix[i + m - 1][0])
            max_product = max(max_product, maxx * suffix[i + m - 1][1])
            
        return max_product
        
# solution = Solution()
# nums = [-1,-9,2,3,-2,-3,1]
# m = 1
# nums = [1,3,-5,5,6,-4]
# m = 3
# nums = [2,-1,2,-6,5,2,-5,7]
# m = 2
# print(solution.maximumProduct(nums, m))