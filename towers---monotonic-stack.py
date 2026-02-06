# 2865. Beautiful Towers I
# Medium

# You are given an array heights of n integers representing the number of bricks in n consecutive towers. Your task is to remove some bricks to form a mountain-shaped tower arrangement. In this arrangement, the tower heights are non-decreasing, reaching a maximum peak value with one or multiple consecutive towers and then non-increasing.

# Return the maximum possible sum of heights of a mountain-shaped tower arrangement.

# Example 1:

# Input: heights = [5,3,4,1,1]

# Output: 13

# Explanation:

# We remove some bricks to make heights = [5,3,3,1,1], the peak is at index 0.

# Example 2:

# Input: heights = [6,5,3,9,2,7]

# Output: 22

# Explanation:

# We remove some bricks to make heights = [3,3,3,9,2,2], the peak is at index 3.

# Example 3:

# Input: heights = [3,2,5,5,2,3]

# Output: 18

# Explanation:

# We remove some bricks to make heights = [2,2,5,5,2,2], the peak is at index 2 or 3.

# Constraints:

# 1 <= n == heights.length <= 103
# 1 <= heights[i] <= 109

from typing import List

class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        max_sum = 0
        for i in range(len(heights)):
            cur_min = heights[i]
            
            cur_sum = 0
            for j in range(i, len(heights)):
                cur_min = min(cur_min, heights[j])
                cur_sum += cur_min
                
            cur_min = heights[i]
            for j in range(i - 1, -1, -1):
                cur_min = min(cur_min, heights[j])
                cur_sum += cur_min
                
            max_sum = max(max_sum, cur_sum)
            
        return max_sum
            
           