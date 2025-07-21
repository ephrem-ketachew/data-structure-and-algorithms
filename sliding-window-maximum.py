# 239. Sliding Window Maximum
# Hard
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

from typing import List
import heapq
from collections import defaultdict

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        deleted = defaultdict(int)
        for i in range(k):
            heapq.heappush(heap, -nums[i])
            
        ans = [-heap[0]]
        
        for i in range(k, len(nums)):
            heapq.heappush(heap, -nums[i])
            deleted[nums[i - k]] += 1
            while deleted[-heap[0]] > 0:
                num = -heapq.heappop(heap)
                deleted[num] -= 1
            ans.append(-heap[0])
            
        return ans
    
# solution = Solution()
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# nums = [1]
# k = 1
# print(solution.maxSlidingWindow(nums, k))