# 2762. Continuous Subarrays
# Medium
# You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

# Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
# Return the total number of continuous subarrays.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [5,4,2,4]
# Output: 8
# Explanation: 
# Continuous subarray of size 1: [5], [4], [2], [4].
# Continuous subarray of size 2: [5,4], [4,2], [2,4].
# Continuous subarray of size 3: [4,2,4].
# There are no subarrys of size 4.
# Total continuous subarrays = 4 + 3 + 1 = 8.
# It can be shown that there are no more continuous subarrays.
 

# Example 2:

# Input: nums = [1,2,3]
# Output: 6
# Explanation: 
# Continuous subarray of size 1: [1], [2], [3].
# Continuous subarray of size 2: [1,2], [2,3].
# Continuous subarray of size 3: [1,2,3].
# Total continuous subarrays = 3 + 2 + 1 = 6.

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109

from typing import List
import heapq
from collections import defaultdict

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        min_heap, max_heap = [], []
        freq = defaultdict(int)
        left, count = 0, 0
        
        def __get_max():
            while max_heap and freq[-max_heap[0]] == 0:
                heapq.heappop(max_heap)
            return -max_heap[0] if max_heap else None
        
        def __get_min():
            while min_heap and freq[min_heap[0]] == 0:
                heapq.heappop(min_heap)
            return min_heap[0] if min_heap else None
        
        for right in range(len(nums)):
            freq[nums[right]] += 1
            heapq.heappush(min_heap, nums[right])
            heapq.heappush(max_heap, -nums[right])
            
            while __get_max() and __get_min() and __get_max() - __get_min() > 2:
                freq[nums[left]] -= 1
                left += 1
                
            count += right - left + 1
            
        return count
    
# solution = Solution()
# nums = [5,4,2,4]
# nums = [1,2,3]
# print(solution.continuousSubarrays(nums))