# 75. Sort Colors

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 
def sortColors(nums):
    start = 0
    end = len(nums) - 1
    color = 0
    
    
    while start < end:
        while start < len(nums) and nums[start] == color:
            start += 1
        if start < end and nums[end] == color:
            temp = nums[start]
            nums[start] = color
            nums[end] = temp
            end -= 1
            start += 1
        else:
            end -= 1
            
    if start < len(nums) and nums[start] == color:
        start += 1
    color = 1
    end = len(nums) - 1
    
    while start < end:
        while start < len(nums) and nums[start] == color:
            start += 1
        if start < end and nums[end] == color:
            temp = nums[start]
            nums[start] = color
            nums[end] = temp
            end -= 1
            start += 1
        else:
            end -= 1
        
    # print(nums)
            
    
# print(sortColors([1,0,0]))