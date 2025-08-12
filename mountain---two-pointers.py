# 845. Longest Mountain in Array
# Medium

# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

# Example 1:

# Input: arr = [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# Example 2:

# Input: arr = [2,2,2]
# Output: 0
# Explanation: There is no mountain.

# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104

# Follow up:

# Can you solve it using only one pass?
# Can you solve it in O(1) space?

from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        max_len = 0
        
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
                j = i - 1
                while j - 1 >= 0 and arr[j - 1] < arr[j]:
                    j -= 1
                    
                k = i + 1
                while k + 1 < len(arr) and arr[k + 1] < arr[k]:
                    k += 1
                    
                max_len = max(max_len, k - j + 1)
                
        return max_len                    
                
# solution = Solution()
# arr = [2,1,4,7,3,2,5]
# print(solution.longestMountain(arr))