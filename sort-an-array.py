# 912. Sort an Array

# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104
from typing import List
# import random

class Solution:
    # No matter how hard I try to solve this question wth Quick Sort(as it uses O(log n) space), I couldn't fix the TLE on leetcode, so I ended up solving it with Merge Sort
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(list1, list2):
            left = right = 0
            merged_list = []
            while left < len(list1) and right < len(list2):
                if list1[left] <= list2[right]:
                    merged_list.append(list1[left])
                    left += 1
                else:
                    merged_list.append(list2[right])
                    right += 1
            
            while left < len(list1):
                merged_list.append(list1[left])
                left += 1
                
            while right < len(list2):
                merged_list.append(list2[right])
                right += 1
                
            return merged_list
        
        def __merge_sort(nums):
            if(len(nums) > 1):
                mid = len(nums) // 2
                left_list = __merge_sort(nums[0 : mid])
                right_list = __merge_sort(nums[mid : len(nums)])
                return merge(left_list, right_list)
            else:
                return nums
        return __merge_sort(nums)
    
        # Optimized Quick Sort Algorithm
        # def partition(nums, left, right):
        #     random_index = random.randint(left, right)
        #     nums[random_index], nums[left] = nums[left], nums[random_index]
                        
        #     pivot = nums[left]
        #     swap_index = left
            
        #     for i in range(left + 1, right + 1):
        #         if nums[i] < pivot:
        #             swap_index += 1
        #             nums[swap_index], nums[i] = nums[i], nums[swap_index]
        #     nums[left], nums[swap_index] = nums[swap_index], nums[left]
        #     return swap_index
        
        # def quick_sort(nums, left, right):
        #     if left < right:
        #         pivot_index = partition(nums, left, right)
        #         quick_sort(nums, left, pivot_index - 1)
        #         quick_sort(nums, pivot_index + 1, right)
                
        # quick_sort(nums, 0, len(nums) - 1)
        # return nums
    
    
    
    #the stupidest and awkward solution for quick sort
#         def pivot(nums, pivot_index, end_index):
#             swap_index = pivot_index
#             for i in range(pivot_index, end_index + 1):
#                 if nums[i] > nums[pivot_index] and swap_index == pivot_index:
#                     swap_index = i
#                 if nums[i] < nums[pivot_index] and swap_index != pivot_index:
#                     nums[swap_index], nums[i] = nums[i], nums[swap_index]
#                     swap_index += 1
#             if swap_index > pivot_index:
#                 nums[pivot_index], nums[swap_index - 1] = nums[swap_index - 1], nums[pivot_index]
#                 return swap_index - 1
#             nums[end_index], nums[swap_index] = nums[swap_index], nums[end_index]
#             return end_index
        
#         def __sort(nums, begin, end):
#             pivot_index = pivot(nums, begin, end)
#             if pivot_index - begin > 1:
#                 __sort(nums, begin, pivot_index - 1 )
#             if end - pivot_index > 1:
#                 __sort(nums, pivot_index + 1, end)
                
#         __sort(nums, 0, len(nums) - 1)