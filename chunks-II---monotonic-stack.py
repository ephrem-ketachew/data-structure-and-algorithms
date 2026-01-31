# 768. Max Chunks To Make Sorted II
# Hard

# You are given an integer array arr.

# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

# Return the largest number of chunks we can make to sort the array.

# Example 1:

# Input: arr = [5,4,3,2,1]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
# Example 2:

# Input: arr = [2,1,3,4,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [2, 1], [3, 4, 4].
# However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
 

# Constraints:

# 1 <= arr.length <= 2000
# 0 <= arr[i] <= 108

from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        min_arr = [arr[-1]] * n
        cur_min = arr[-1]
        for i in range(n - 2, -1, -1):
            cur_min = min(arr[i], min_arr[i + 1])
            min_arr[i] = cur_min
        
        partition = 0
        cur_max = 0
        for i, num in enumerate(arr):
            cur_max = max(cur_max, num)
            if i + 1 == n or cur_max <= min_arr[i + 1]:
                partition += 1
                
        return partition
        