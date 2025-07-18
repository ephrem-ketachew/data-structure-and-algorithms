# 2831. Find the Longest Equal Subarray
# Medium

# You are given a 0-indexed integer array nums and an integer k.

# A subarray is called equal if all of its elements are equal. Note that the empty subarray is an equal subarray.

# Return the length of the longest possible equal subarray after deleting at most k elements from nums.

# A subarray is a contiguous, possibly empty sequence of elements within an array.

# Example 1:

# Input: nums = [1,3,2,3,1,3], k = 3
# Output: 3
# Explanation: It's optimal to delete the elements at index 2 and index 4.
# After deleting them, nums becomes equal to [1, 3, 3, 3].
# The longest equal subarray starts at i = 1 and ends at j = 3 with length equal to 3.
# It can be proven that no longer equal subarrays can be created.
# Example 2:

# Input: nums = [1,1,2,2,1,1], k = 2
# Output: 4
# Explanation: It's optimal to delete the elements at index 2 and index 3.
# After deleting them, nums becomes equal to [1, 1, 1, 1].
# The array itself is an equal subarray, so the answer is 4.
# It can be proven that no longer equal subarrays can be created.
 
# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= nums.length
# 0 <= k <= nums.length

from typing import List
from collections import defaultdict

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        max_len = 0
        left = 0
        max_freq = 0
        
        for right in range(len(nums)):
            c = counter[nums[right]] = counter[nums[right]] + 1
            max_freq = max(max_freq, c)
            
            while (right - left + 1) - max_freq > k:
                counter[nums[left]] -= 1
                left += 1
                
            max_len = max(max_len, c)
            
        return max_len
    
# solution = Solution()
# nums = [2,2,1]
# k = 1
# print(solution.longestEqualSubarray(nums, k))