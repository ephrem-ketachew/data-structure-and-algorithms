# 658. Find K Closest Elements
# Medium

# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3

# Output: [1,2,3,4]

# Example 2:

# Input: arr = [1,1,2,3,4,5], k = 4, x = -1

# Output: [1,1,2,3]

# Constraints:

# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr is sorted in ascending order.
# -104 <= arr[i], x <= 104

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # def bs(nums, key):
        #     begin, end = 0, len(nums) - 1
        #     while begin <= end:
        #         mid = (begin + end) // 2
        #         if nums[mid] == key:
        #             return mid
        #         elif nums[mid] > key:
        #             end = mid - 1
        #         else:
        #             begin = mid + 1
        #     return begin
        
        # k_closest = []
        # index = bs(arr, x)
     
        # left = index - 1
        # right = index
        # while len(k_closest) < k:
        #     if left >= 0 and right < len(arr):
        #         if abs(arr[left] - x) <= abs(arr[right] - x):
        #             k_closest.append(arr[left])
        #             left -= 1
        #         else:
        #             k_closest.append(arr[right])
        #             right += 1
            
        #     elif left >= 0:
        #         k_closest.append(arr[left])
        #         left -= 1
        #     else:
        #         k_closest.append(arr[right])
        #         right += 1
                
        # k_closest.sort()
        # return k_closest
        
        
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            # arr[mid:mid+k](sliding window)
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
            
        return arr[left:left + k]
    
# solution = Solution()
# arr = [1,2,3,4,5]
# k = 4
# x = 3
# arr = [1,1,2,3,4,5]
# k = 4
# x = -1

# arr = [0,1,1,1,2,3,6,7,8,9]
# k = 9
# x = 4

# arr = [0,0,1,2,3,3,4,7,7,8]
# k = 3
# x = 5
# print(solution.findClosestElements(arr, k, x))