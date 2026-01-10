# 3101. Count Alternating Subarrays
# Medium

# You are given a binary array nums.

# We call a subarray alternating if no two adjacent elements in the subarray have the same value.

# Return the number of alternating subarrays in nums.

# Example 1:

# Input: nums = [0,1,1,1]

# Output: 5

# Explanation:

# The following subarrays are alternating: [0], [1], [1], [1], and [0,1].

# Example 2:

# Input: nums = [1,0,1,0]

# Output: 10

# Explanation:

# Every subarray of the array is alternating. There are 10 possible subarrays that we can choose.

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

from typing import List

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        count = 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                k += 1
            else:
                count += k * (k + 1) // 2
                k = 1
        count += k * (k + 1) // 2
        
        return count