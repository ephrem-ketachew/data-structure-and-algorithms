# 303. Range Sum Query - Immutable

# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.running_sum = [0] * (len(self.nums) + 1)
        
        for i in range(len(self.nums)):
            self.running_sum[i + 1] = self.running_sum[i] + self.nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.running_sum[right + 1] - self.running_sum[left]
    

# # [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]    
# n = NumArray([-2, 0, 3, -5, 2, -1])
# print(n.sumRange(0, 2))
# print(n.sumRange(2, 5))
# print(n.sumRange(0, 5))