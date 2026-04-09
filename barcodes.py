# 1054. Distant Barcodes
# Medium

# In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

# Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

# Example 1:

# Input: barcodes = [1,1,1,2,2,2]
# Output: [2,1,2,1,2,1]
# Example 2:

# Input: barcodes = [1,1,1,1,2,2,3,3]
# Output: [1,3,1,3,1,2,1,2]

# Constraints:

# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000

from typing import List
from collections import Counter
import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # counter = Counter(barcodes)
        # heap = []
        # for num in counter:
        #     heapq.heappush(heap, (-counter[num], num))
            
        # ans = []
        # while heap:
        #     first_freq, first_num = heapq.heappop(heap)
        #     ans.append(first_num)
        #     first_freq = first_freq * -1 - 1
            
        #     if heap:
        #         second_freq, second_num = heapq.heappop(heap)
        #         ans.append(second_num)
        #         second_freq = second_freq * -1 - 1
                
        #         if second_freq > 0:
        #             heapq.heappush(heap, (-second_freq, second_num))
             
        #     if first_freq > 0:       
        #         heapq.heappush(heap, (-first_freq, first_num))
                
        # return ans
        
        counter = Counter(barcodes)
        sorted_barcodes = sorted(counter.items(), key=lambda x: -x[1])
        n = len(barcodes)
        ans = [0] * n
        pos = 0
        for code, freq in sorted_barcodes:
            for _ in range(freq):
                if pos >= n:
                    pos = 1
                ans[pos] = code
                pos += 2
                
        return ans