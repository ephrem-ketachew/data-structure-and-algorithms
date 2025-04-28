# 713. Subarray Product Less Than K
# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0

def numSubarrayProductLessThanK(nums, k):
    left = 0
    window_product = 1
    count_subarrays = 0
    
    for right in range(len(nums)):
        window_product *= nums[right]
        
        while left <= right and  window_product >= k:
            window_product /= nums[left]
            left += 1
            
        count_subarrays += right - left + 1
    
    return count_subarrays

# print(numSubarrayProductLessThanK([10,5,2,6], 100))
            
    