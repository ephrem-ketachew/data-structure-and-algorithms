# 3364. Minimum Positive Sum Subarray 
# Easy
# You are given an integer array nums and two integers l and r. Your task is to find the minimum sum of a subarray whose size is between l and r (inclusive) and whose sum is greater than 0.

# Return the minimum sum of such a subarray. If no such subarray exists, return -1.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [3, -2, 1, 4], l = 2, r = 3

# Output: 1

# Explanation:

# The subarrays of length between l = 2 and r = 3 where the sum is greater than 0 are:

# [3, -2] with a sum of 1
# [1, 4] with a sum of 5
# [3, -2, 1] with a sum of 2
# [-2, 1, 4] with a sum of 3
# Out of these, the subarray [3, -2] has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.

# Example 2:

# Input: nums = [-2, 2, -3, 1], l = 2, r = 3

# Output: -1

# Explanation:

# There is no subarray of length between l and r that has a sum greater than 0. So, the answer is -1.

# Example 3:

# Input: nums = [1, 2, 3, 4], l = 2, r = 4

# Output: 3

# Explanation:

# The subarray [1, 2] has a length of 2 and the minimum sum greater than 0. So, the answer is 3.

# Constraints:

# 1 <= nums.length <= 100
# 1 <= l <= r <= nums.length
# -1000 <= nums[i] <= 1000

from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        l_win_sum = sum(nums[:l])
        if l_win_sum > 0:
            min_sum = l_win_sum
            
        for i in range(l, len(nums)):
            l_win_sum += nums[i]
            l_win_sum -= nums[i - l]
            
            if l_win_sum > 0:
                min_sum = min(min_sum, l_win_sum)
            
            win_sum = l_win_sum
            for j in range(i - l, max(i - r, -1), -1):
                win_sum += nums[j]
                if win_sum > 0:
                    min_sum = min(min_sum, win_sum)
                
            if min_sum == 1:
                return 1
            
        return min_sum if min_sum != float('inf') else -1
    
    
# nums = [25,-9]
# l = 1
# r = 1

# nums = [-6,23,-8,-4,-12]
# l = 1
# r = 3
# solution = Solution()
# print(solution.minimumSumSubarray(nums, l, r))