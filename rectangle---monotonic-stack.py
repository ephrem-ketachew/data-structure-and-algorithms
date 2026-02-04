# 84. Largest Rectangle in Histogram
# Hard

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Example 1:

# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4
 

# Constraints:

# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights += [float('-inf')]
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                mid_idx = stack.pop()
                
                left_bound = stack[-1] + 1 if stack else 0
                right_bound = i - 1
                
                area = (right_bound - left_bound + 1) * heights[mid_idx]
                max_area = max(max_area, area)
                
            stack.append(i)
                
        return max_area