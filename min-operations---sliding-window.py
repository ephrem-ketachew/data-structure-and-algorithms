# 1658. Minimum Operations to Reduce X to Zero
# Medium
# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

# Example 1:

# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
# Example 2:

# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# Example 3:

# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
# 1 <= x <= 109

from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        summ = sum(nums)

        if summ < x:
            return -1
            
        target = summ - x
        win_sum, left, max_len = 0, 0, -1
        
        for right in range(len(nums)):
            win_sum += nums[right]
            while win_sum > target:
                win_sum -= nums[left]
                left += 1
            
            if win_sum == target:
                max_len = max(max_len, right - left + 1)
        
        return len(nums) - max_len if max_len != -1 else -1
            
# solution = Solution()
# nums = [1,1,4,2,3]
# x = 5
# nums = [1,1]
# x = 3
# print(solution.minOperations(nums, x))