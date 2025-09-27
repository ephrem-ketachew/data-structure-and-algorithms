# 812. Largest Triangle Area
# Easy
# Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

# Example 1:


# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2.00000
# Explanation: The five points are shown in the above figure. The red triangle is the largest.
# Example 2:

# Input: points = [[1,0],[0,0],[0,1]]
# Output: 0.50000
 

# Constraints:

# 3 <= points.length <= 50
# -50 <= xi, yi <= 50
# All the given points are unique.

from typing import List
from math import sqrt

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def calc_area(point1, point2, point3):
            p1x, p1y = point1
            p2x, p2y = point2
            p3x, p3y = point3
            
            return abs(
                p1x * (p2y - p3y) +
                p2x * (p3y - p1y) +
                p3x * (p1y - p2y)
            ) / 2
    
            # a = sqrt((p1x - p2x) * (p1x - p2x) + (p1y - p2y) * (p1y - p2y))
            # b = sqrt((p1x - p3x) * (p1x - p3x) + (p1y - p3y) * (p1y - p3y))
            # c = sqrt((p3x - p2x) * (p3x - p2x) + (p3y - p2y) * (p3y - p2y))
            
            # s = (a + b + c) / 2
            
            # return s * (s - a) * (s - b) * (s - c)
        
        max_area = 0
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    max_area = max(max_area, calc_area(points[i], points[j], points[k]))
                    
        return max_area
        # return sqrt(max_area)
        