# 1679. Max Number of K-Sum Pairs
# Medium
# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
 
# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109

from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # counter = Counter(nums)
        # keys = sorted(counter.keys())
        
        # count = 0
        # left, right = 0, len(keys) - 1
        # while left <= right:
        #     summ = keys[left] + keys[right]
        #     if summ == k:
        #         if left == right:
        #             count += counter[keys[left]] // 2
        #         else:
        #             count += min(counter[keys[left]], counter[keys[right]])
        #         left += 1
        #         right -= 1
        #     elif summ < k:
        #         left += 1
        #     else:
        #         right -= 1
                
        # return count
        
        # counter = Counter()
        # count = 0
        # for num in nums:
        #     complement = k - num
        #     if counter[complement] > 0:
        #         count += 1
        #         counter[complement] -= 1
        #     else:
        #         counter[num] += 1
                
        # return count
        
        counter = Counter(nums)
        arr = counter.keys()
        count = 0
        for num in arr:
            complement = k - num
            if counter[complement] > 0:
                if num == complement:
                    count += counter[num] // 2
                else:
                    count += min(counter[num], counter[complement]) 
            counter[num] = 0
                    
        return count
    
# solution = Solution()
# nums = [3,1,3,4,3]
# k = 6
# print(solution.maxOperations(nums, k))