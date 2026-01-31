# 42. Trapping Rain Water
# Hard

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 
# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        stack = []
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                floor_idx = stack.pop()
                if not stack:
                    break
                left_wall = stack[-1]
                right_wall = i
                
                cur_height = min(height[left_wall], height[right_wall]) - height[floor_idx]
                width = right_wall - left_wall - 1
                
                area += cur_height * width
                
            stack.append(i)
            
        return area
    
# s = Solution()
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(s.trap(height))