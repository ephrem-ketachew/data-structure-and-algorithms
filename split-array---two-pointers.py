# 1712. Ways to Split Array Into Three Subarrays
# Medium
# A split of an integer array is good if:

# The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
# The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
# Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.

# Example 1:

# Input: nums = [1,1,1]
# Output: 1
# Explanation: The only good way to split nums is [1] [1] [1].
# Example 2:

# Input: nums = [1,2,2,2,5,0]
# Output: 3
# Explanation: There are three good ways of splitting nums:
# [1] [2] [2,2,5,0]
# [1] [2,2] [2,5,0]
# [1,2] [2,2] [5,0]
# Example 3:

# Input: nums = [3,2,1]
# Output: 0
# Explanation: There is no good way to split nums.

# Constraints:

# 3 <= nums.length <= 105
# 0 <= nums[i] <= 104

from typing import List
import bisect

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        # BRUTE FORCE only to TLE😭
        # count = 0
        
        # summ = sum(nums)
        # n = len(nums)
        
        # left = middle = 0
        # for i in range(n - 2):
        #     left += nums[i]
        #     j = i + 1
        #     middle = 0
        #     while j < n - 1 and middle < left:
        #         middle += nums[j]
        #         j += 1
                
        #     j = max(j, i + 2)
        #     while j < n and summ - (left + middle) >= middle >= left:
        #         count += 1
                
        #         middle += nums[j]
                
        #         j += 1
                
        # return count
        
        MOD = 10 ** 9 + 7
        
        count = 0
        n = len(nums)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            
        # for i in range(1, n - 1):
   
        #     l = bisect.bisect_left(prefix, 2 * prefix[i], lo=i + 1, hi=n)
        #     r = bisect.bisect_right(prefix, (prefix[i] + prefix[n]) / 2, lo=i + 1, hi=n) - 1
            
        #     if l <= r:
        #         count += r - l + 1
        #         count %= MOD
                
        # return count
        
        l = r = 1
        for i in range(1, n - 1):
            
            l = max(l, i + 1)
            while l < n and prefix[l] < 2 * prefix[i]:
                l += 1
                
            r = max(r, l)
            while r < n and prefix[r] <= (prefix[i] + prefix[n]) / 2:
                r += 1
                
            if r > l:
                count += r - l
                count %= MOD
                
        return count    
       

    
# solution = Solution()
# nums = [1,1,1]
# nums = [1,2,2,2,5,0]
# nums = [3,2,1]
# nums = [0,3,3]
# nums = [7,0,5]
# print(solution.waysToSplit(nums))
