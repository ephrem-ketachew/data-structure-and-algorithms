# 611. Valid Triangle Number

# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

# Example 1:

# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Example 2:

# Input: nums = [4,2,3,4]
# Output: 4

def triangleNumber(nums):
    output = 0
    nums.sort()
    
    for i in range(len(nums) - 1, 1, -1):
        start = 0
        end = i - 1
        
        while start < end:
            s = nums[start] + nums[end]
            
            if s > nums[i]:
                output += end - start
                end -= 1
            else:
                start += 1
                
    return output

# print(triangleNumber([2,2,3,4]))