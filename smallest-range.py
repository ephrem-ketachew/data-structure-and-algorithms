# 910. Smallest Range II
# Medium
# You are given an integer array nums and an integer k.

# For each index i where 0 <= i < nums.length, change nums[i] to be either nums[i] + k or nums[i] - k.

# The score of nums is the difference between the maximum and minimum elements in nums.

# Return the minimum score of nums after changing the values at each index.

# Example 1:

# Input: nums = [1], k = 0
# Output: 0
# Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.
# Example 2:

# Input: nums = [0,10], k = 2
# Output: 6
# Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.
# Example 3:

# Input: nums = [1,3,6], k = 3
# Output: 3
# Explanation: Change nums to be [4, 6, 3]. The score is max(nums) - min(nums) = 6 - 3 = 3.

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 104
# 0 <= k <= 104

from typing import List

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        # I was greedily deciding +k or -k for each number based on the local range.
        # But UNFORTUNATELY😭, this approach doesn’t always give the right minimum score.
        # WASTED MORE THAN AN HOUR
        # nums.sort()
        
        # nums[0] += k
        # min_val = max_val = nums[0]
    
        # for i in range(1, len(nums)):
        #     add_range = max(max_val, nums[i] + k) - min(min_val, nums[i] + k)
        #     sub_range = max(max_val, nums[i] - k) - min(min_val, nums[i] - k)
            
        #     if(add_range < sub_range):
        #         nums[i] += k
        #     elif(add_range > sub_range):
        #         nums[i] -= k
        #     else:
        #         if nums[i] + k >= nums[-1]:
        #             nums[i] -= k
        #         else:
        #             nums[i] += k
                
        #     min_val = min(min_val, nums[i])
        #     max_val = max(max_val, nums[i])

        # return max_val - min_val
        
        nums.sort()
        ans = nums[-1] - nums[0]
        
        for i in range(1, len(nums)):
            min_val = min(nums[i] - k, nums[0] + k)
            max_val = max(nums[i - 1] + k, nums[-1] - k)
            ans = min(ans, max_val - min_val)
            
        return ans
    
# solution = Solution()
# nums = [1]
# k = 0
# nums = [0,10]
# k = 2
# nums = [1,3,6]
# k = 3
# nums = [4,1,8,10]
# k = 3
# nums = [1,4,6,4]
# k = 3
# nums = [7,8,8,5,2]
# k = 4
# print(solution.smallestRangeII(nums, k))