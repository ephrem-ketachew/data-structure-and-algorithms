# Q2. Count Number of Trapezoids I
# Medium
# 4 pt.
# You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

# A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

# Return the number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.

# Since the answer may be very large, return it modulo 109 + 7.

# Example 1:

# Input: points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

# Output: 3

# Explanation:

# There are three distinct ways to pick four points that form a horizontal trapezoid:

# Using points [1,0], [2,0], [3,2], and [2,2].
# Using points [2,0], [3,0], [3,2], and [2,2].
# Using points [1,0], [3,0], [3,2], and [2,2].
# Example 2:

# Input: points = [[0,0],[1,0],[0,1],[2,1]]

# Output: 1

# Explanation:
    
# There is only one horizontal trapezoid that can be formed.

# Constraints:

# 4 <= points.length <= 105
# –108 <= xi, yi <= 108
# All points are pairwise distinct.©leetcode

from typing import List
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        counter = defaultdict(int)
        
        for (x, y) in points:
            counter[y] += 1
            
        y_pt_count = list(counter.values())
        count_lines = [0] * len(y_pt_count)
        
        for i, pt_c in enumerate(y_pt_count):
            if pt_c == 1:
                continue
            count_line = (pt_c * (pt_c - 1)) // 2
            count_lines[i] = count_line
        
        count_trapezoid = 0
        
        summ = sum(count_lines)
        prefix = 0
        
        
        for count in count_lines:
            prefix += count
            count_trapezoid += count * (summ - prefix)
                
        return count_trapezoid % MOD
        
                
# solution = Solution()
# points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
# points = [[0,0],[1,0],[0,1],[2,1]]
# print(solution.countTrapezoids(points))