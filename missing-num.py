# 1539. Kth Missing Positive Number
# Easy

# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Return the kth positive integer that is missing from this array.

# Example 1:

# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
# Example 2:

# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

# Constraints:

# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# arr[i] < arr[j] for 1 <= i < j <= arr.length

# Follow up:

# Could you solve this problem in less than O(n) complexity?

from typing import List
from bisect import bisect_left

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # cur = 0
        # count = 0
        # for i in range(len(arr)):
        #     while cur < arr[i] - 1:
        #         cur += 1
        #         count += 1
                
        #         if count == k:
        #             return cur
                
        #     cur = arr[i]
                
        # while count < k:
        #     cur += 1
        #     count += 1
            
        # return cur
        
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
                
        return left + k
        