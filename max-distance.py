# 3464. Maximize the Distance Between Points on a Square
# Hard

# You are given an integer side, representing the edge length of a square with corners at (0, 0), (0, side), (side, 0), and (side, side) on a Cartesian plane.

# You are also given a positive integer k and a 2D integer array points, where points[i] = [xi, yi] represents the coordinate of a point lying on the boundary of the square.

# You need to select k elements among points such that the minimum Manhattan distance between any two points is maximized.

# Return the maximum possible minimum Manhattan distance between the selected k points.

# The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.

# Example 1:

# Input: side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4

# Output: 2

# Explanation:



# Select all four points.

# Example 2:

# Input: side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4

# Output: 1

# Explanation:

# Select the points (0, 0), (2, 0), (2, 2), and (2, 1).

# Example 3:

# Input: side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5

# Output: 1

# Explanation:

# Select the points (0, 0), (0, 1), (0, 2), (1, 2), and (2, 2).

# Constraints:

# 1 <= side <= 109
# 4 <= points.length <= min(4 * side, 15 * 103)
# points[i] == [xi, yi]
# The input is generated such that:
# points[i] lies on the boundary of the square.
# All points[i] are unique.
# 4 <= k <= min(25, points.length)

from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        arr = []
        for x, y in points:
            if x == 0:
                arr.append(y)
            elif y == side:
                arr.append(side + x)
            elif x == side:
                arr.append(2 * side + (side - y))
            else:
                arr.append(3 * side + (side - x))
                
        arr.sort()
        n = len(arr)
        def check(d: int) -> bool:
            nxt = [n] * n
            j = 0
            for i in range(n):
                while j < n and arr[j] - arr[i] < d:
                    j += 1
                nxt[i] = j
                
            for start_idx in range(n):
                if arr[start_idx] > arr[0] + d:
                    break
                
                curr_idx = start_idx
                count = 1
                for _ in range(k - 1):
                    curr_idx = nxt[curr_idx]
                    if curr_idx == n:
                        break
                    count += 1
                    
                if count == k and (arr[start_idx] + 4 * side - arr[curr_idx] >= d):
                    return True
                
            return False
            
        low, high = 1, (4 * side) // 4
        while low < high:
            mid = (low + high + 1) // 2
            if check(mid):
                low = mid
            else:
                high = mid - 1
                
        return low