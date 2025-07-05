# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # appraoch 1 simple yet o(n square) time complexity
        # top_k_items = sorted(Counter(nums).items(), key = lambda x: x[1], reverse=True)[:k]
        # return [el[0] for el in top_k_items]
        
        
        # approach 2.... 
        # heap = []
        # for num, freq in Counter(nums).items():
        #     heapq.heappushpop(heap, [freq, num]) if len(heap) >= k else heapq.heappush(heap, [freq, num])                
        
        # return [heapq.heappop(heap)[1] for _ in range(k)]
    
        # approach 3... the most effiecient approach o(n) time complexity
        counter = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in counter.items():
            bucket[freq].append(num)
            
        res = []
        for i in range(len(bucket) - 1, - 1, -1):
            for num in bucket[i]:
                res.append(num)
            if len(res) == k:
                return res
        
        
        # my first approach... get ac but inefficient(2months ago)
        # freq = Counter(nums)
        # freq_vals = freq.values()
        # heap = []
        # for val in freq_vals:
        #     heapq.heappush(heap, -val)
            
        # output = []
        # keys = []
        # for i in range(k):
        #     f = -heapq.heappop(heap)
        #     keys2 = [k for k, v in freq.items() if v == f]
        #     if not keys:
        #         output.append(keys2.pop())
        #         keys = keys2
        #     else:
        #         output.append(keys.pop())
                
        # return output
        
        
                
# s = Solution()
# print(s.topKFrequent([1,2], 2))