# 740. Delete and Earn
# Medium

# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.

# Example 1:

# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
# Example 2:

# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.
 
# Constraints:

# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] <= 104

from typing import List
from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        unique_nums = sorted(set(nums))
        m = len(unique_nums)
        if m == 1:
            return sum(nums)
        
        dp = [0] * m
        dp[0] = unique_nums[0] * counter[unique_nums[0]]
        max_seen1, max_seen2 = 0, dp[0]
        for i in range(1, m):
            dp[i] = unique_nums[i] * counter[unique_nums[i]]
            if unique_nums[i] - unique_nums[i - 1] > 1:
                dp[i] += max_seen2
            else:
                dp[i] += max_seen1
                
            max_seen1 = max_seen2
            max_seen2 = max(max_seen2, dp[i])
            
        return max(dp)