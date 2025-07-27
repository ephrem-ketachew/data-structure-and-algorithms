# 2357. Make Array Zero by Subtracting Equal Amounts
# Easy

# You are given a non-negative integer array nums. In one operation, you must:

# Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
# Subtract x from every positive element in nums.
# Return the minimum number of operations to make every element in nums equal to 0.

# Example 1:

# Input: nums = [1,5,0,3,5]
# Output: 3
# Explanation:
# In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
# In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
# In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
# Example 2:

# Input: nums = [0]
# Output: 0
# Explanation: Each element in nums is already 0 so no operations are needed.

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

from typing import List
# import heapq

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # heapq.heapify(nums)
        # while nums and nums[0] == 0:
        #     heapq.heappop(nums)
        
        # ops = 0
        # while nums:
        #     minn = heapq.heappop(nums)
        #     temp = []
        #     while nums:
        #         temp.append(heapq.heappop(nums) - minn)
            
        #     for num in temp:
        #         if num:
        #             heapq.heappush(nums, num)
                
        #     ops += 1
            
        # return ops
        
        uniques = set(nums)
        return len(uniques) - 1 if 0 in nums else len(uniques)
    
# solution = Solution()
# nums = [1,5,0,3,5]
# nums = [0]
# print(solution.minimumOperations(nums))