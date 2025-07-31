# 1574. Shortest Subarray to be Removed to Make Array Sorted
# Medium
# Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

# Return the length of the shortest subarray to remove.

# A subarray is a contiguous subsequence of the array.

# Example 1:

# Input: arr = [1,2,3,10,4,2,3,5]
# Output: 3
# Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
# Another correct solution is to remove the subarray [3,10,4].
# Example 2:

# Input: arr = [5,4,3,2,1]
# Output: 4
# Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
# Example 3:

# Input: arr = [1,2,3]
# Output: 0
# Explanation: The array is already non-decreasing. We do not need to remove any elements.

# Constraints:

# 1 <= arr.length <= 105
# 0 <= arr[i] <= 109

from typing import List
import bisect

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n - 1
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                break
            left = i
            
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                break
            right = i
            
        arr_right = arr[right:]
        if left >= right:
            return 0
        
        count = right - left - 1
        
        minn = min(left + 1, len(arr))
        for i in range(left + 1):
            index = bisect.bisect_left(arr_right, arr[i])
            minn = min(minn, left - i + index)

        return count + minn
    
    
# solution = Solution()
# arr = [1,2,3,10,4,2,3,5]
# arr = [2,2,2,1,1,1]
# print(solution.findLengthOfShortestSubarray(arr))