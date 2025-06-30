# 594. Longest Harmonious Subsequence
# Easy
# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

# Example 1:

# Input: nums = [1,3,2,2,5,2,3,7]

# Output: 5

# Explanation:

# The longest harmonious subsequence is [3,2,2,2,3].

# Example 2:

# Input: nums = [1,2,3,4]

# Output: 2

# Explanation:

# The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

# Example 3:

# Input: nums = [1,1,1,1]

# Output: 0

# Explanation:

# No harmonic subsequence exists.

 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -109 <= nums[i] <= 109

from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # approach 1 o(n(logn)) sliding window and sorting
        # nums.sort()
        # max_length = 0
        # left = 0
        
        # for right in range(len(nums)):
        #     while left <= right and nums[right] - nums[left] > 1:
        #         left += 1
        #     max_length = max(max_length ,right - left + 1) if nums[right] - nums[left] == 1 else max_length
            
        # return max_length
        
        # approach 2 o(n) hash table
        counter = Counter(nums)
        max_length = 0
        for num in counter:
            if num + 1 in counter:
                max_length = max(max_length, counter[num] + counter[num + 1])
                
        return max_length
        
    
# nums = [1,3,2,2,5,2,3,7]
# nums = [1,2,3,4]
# nums = [1,1,1,1]
# solution = Solution()
# print(solution.findLHS(nums))