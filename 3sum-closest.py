# 16. 3Sum Closest
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

def threeSumClosest(nums, target):
    closest_sum = float('inf')
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        start = i + 1
        end = len(nums) - 1
        
        while start < end:           
            total = nums[i] + nums[start] + nums[end]
            if abs(total - target) < abs(closest_sum - target):
                closest_sum = total
           
            if total == target:
                return total
            elif total < target:
                start += 1
            else:
                end -= 1
    
    return closest_sum
 
# print(threeSumClosest([0, 0, 0], 1))