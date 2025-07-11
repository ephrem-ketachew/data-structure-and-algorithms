# 2962. Count Subarrays Where Max Element Appears at Least K Times
# Medium
# You are given an integer array nums and a positive integer k.

# Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

# A subarray is a contiguous sequence of elements within an array.

# Example 1:

# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
# Example 2:

# Input: nums = [1,4,2,1], k = 3
# Output: 0
# Explanation: No subarray contains the element 4 at least 3 times.

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106
# 1 <= k <= 105

from typing import List
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # count_at_most_k_minus_1 = 0
        # target, n, left = max(nums), len(nums), 0
        # counter = defaultdict(int)
        
        # for right in range(n):
        #     counter[nums[right]] += 1
        #     while counter[target] >= k:
        #         counter[nums[left]] -= 1
        #         if counter[nums[left]] == 0:
        #             del counter[nums[left]]
        #         left += 1
                    
        #     count_at_most_k_minus_1 += right - left + 1
            
        # max_subarray_count = n * (n + 1) // 2
        
        # return max_subarray_count - count_at_most_k_minus_1
        
        maximum = max(nums)
        count, left, ans = 0, 0, 0
        
        for right in range(len(nums)):
            if nums[right] == maximum:
                count += 1
                
            while count == k:
                if nums[left] == maximum:
                    count -= 1
                left += 1
                
            ans += left
            
        return ans