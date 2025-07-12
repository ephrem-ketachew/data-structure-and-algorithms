# 34. Find First and Last Position of Element in Sorted Array
# Medium
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # def bs(arr, k):
        #     begin, end = 0, len(arr) - 1
        #     while begin <= end:
        #         mid = (begin + end) // 2
        #         if arr[mid] == k:
        #             return mid
        #         elif arr[mid] > k:
        #             end = mid - 1
        #         else:
        #             begin = mid + 1
            
        #     return -1
        
        # ans = [-1, -1]
        
        # left = right = bs(nums, target)
        
        # # while left > 0 and nums[left - 1] == target:
        # #     left -= 1
        # # ans[0] = left
        
        # # while right < len(nums) - 1 and nums[right + 1] == target:
        # #     right += 1
        # # ans[1] = right
        
        # while left != -1:
        #     ans[0] = left
        #     left = bs(nums[:left], target)
        
        # index = right
        # while index != -1:
        #     ans[1] = right
        #     index = bs(nums[right + 1:], target)
        #     right = index + right + 1
        # return ans
        
        def find_left(arr, k):
            begin, end, ans = 0, len(arr) - 1, -1
            while begin <= end:
                mid = (begin + end) // 2
                if arr[mid] >= k:
                    end = mid - 1
                else:
                    begin = mid + 1
                if arr[mid] == k:
                    ans = mid
                    
            return ans
            
            
        def find_right(arr, k):
            begin, end, ans = 0, len(arr) - 1, -1
            while begin <= end:
                mid = (begin + end) // 2
                if arr[mid] <= k:
                    begin = mid + 1
                else:
                    end = mid - 1
                if arr[mid] == k:
                    ans = mid
                    
            return ans
        
        return [find_left(nums, target), find_right(nums, target)]
    
# solution = Solution()
# nums = [2,2]
# target = 2
# print(solution.searchRange(nums, target))