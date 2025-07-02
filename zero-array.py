# 3356. Zero Array Transformation II
# Medium
# You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

# Each queries[i] represents the following action on nums:

# Decrement the value at each index in the range [li, ri] in nums by at most vali.
# The amount by which each value is decremented can be chosen independently for each index.
# A Zero Array is an array with all its elements equal to 0.

# Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

# Example 1:

# Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

# Output: 2

# Explanation:

# For i = 0 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
# The array will become [1, 0, 1].
# For i = 1 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
# The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.
# Example 2:

# Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

# Output: -1

# Explanation:

# For i = 0 (l = 1, r = 3, val = 2):
# Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
# The array will become [4, 1, 0, 0].
# For i = 1 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
# The array will become [3, 0, 0, 0], which is not a Zero Array.
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 5 * 105
# 1 <= queries.length <= 105
# queries[i].length == 3
# 0 <= li <= ri < nums.length
# 1 <= vali <= 5

from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # k = 0
        # for query in queries:
        #     if max(nums) == 0:
        #         return k
        #     k += 1
        #     for i in range(query[0], query[1] + 1):
        #         if nums[i] != 0:
        #             if nums[i] >= query[2]:
        #                 nums[i] -= query[2]
        #             else:
        #                 nums[i] = 0
            
        # return k if max(nums) == 0 else -1
        
        
        n = len(nums)
        m = len(queries)
        
        def can_zero(k):
            diff = [0] * (n + 1)
            temp = nums[:]
            
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                diff[r + 1] -= val
                
            cur = 0
            for i in range(n):
                cur += diff[i]
                temp[i] = max(temp[i] - cur, 0)
                
            return all(num == 0 for num in temp)
        
        k = -1
        left, right = 0, m
        while left <= right:
            mid = (left + right) // 2
            if can_zero(mid):
                k = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return k