# class Solution:
#     def twoSum(nums,target):
#        for i in range(len(nums)- 1):
#         for j in range(i+1, len(nums)):
#             if(nums[i]+nums[j] == target):
#                 return [i, j]

# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    nums_sorted = nums.copy()
    nums_sorted.sort()
    
    while left < right:
        if nums_sorted[left] + nums_sorted[right] == target:
            num1, num2 = nums_sorted[left], nums_sorted[right]
            break
        elif nums_sorted[left] + nums_sorted[right] < target:
            left += 1
        else:
            right -= 1
        
    return [nums.index(num1), len(nums) - 1 - nums[::-1].index(num2)]

print(twoSum([3, 3],6))