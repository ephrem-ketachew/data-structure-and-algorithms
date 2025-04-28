# 18. 4Sum
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 
def fourSum(nums, target):
    output = []
    nums.sort()
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            start = j + 1
            end = len(nums) - 1
            
            while start < end:
                total = nums[i] + nums[j] + nums[start] + nums[end]
                if total == target:
                    output.append([nums[i], nums[j], nums[start], nums[end]])
                    
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                        
                    start += 1
                    end -= 1
                elif total < target:
                    start += 1
                else:
                    end -= 1
    
    return output

# print(fourSum([2,2,2,2,2], 8))