# 3531. Count Covered Buildings
# Medium

# You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].

# A building is covered if there is at least one building in all four directions: left, right, above, and below.

# Return the number of covered buildings.


# Example 1:

# Input: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]

# Output: 1

# Explanation:

# Only building [2,2] is covered as it has at least one building:
# above ([1,2])
# below ([3,2])
# left ([2,1])
# right ([2,3])
# Thus, the count of covered buildings is 1.
# Example 2:

# Input: n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]

# Output: 0

# Explanation:

# No building has at least one building in all four directions.
# Example 3:

# Input: n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]

# Output: 1

# Explanation:

# Only building [3,3] is covered as it has at least one building:
# above ([1,3])
# below ([5,3])
# left ([3,2])
# right ([3,5])
# Thus, the count of covered buildings is 1.
 

# Constraints:

# 2 <= n <= 105
# 1 <= buildings.length <= 105 
# buildings[i] = [x, y]
# 1 <= x, y <= n
# All coordinates of buildings are unique.

from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        not_covered = set()
        
        sorted_buildings_by_x = sorted(buildings, key=lambda pair: (pair[0], pair[1]))
        prev_x = -1
        for i, (x, y) in enumerate(sorted_buildings_by_x):
            if x != prev_x:
                not_covered.add((x, y))
                if i > 0:
                    not_covered.add((sorted_buildings_by_x[i - 1][0], sorted_buildings_by_x[i - 1][1]))
            prev_x = x
        not_covered.add((sorted_buildings_by_x[-1][0], sorted_buildings_by_x[-1][1]))
        
        sorted_buildings_by_y = sorted(buildings, key=lambda pair: (pair[1], pair[0]))
        prev_y = -1
        for i, (x, y) in enumerate(sorted_buildings_by_y):
            if y != prev_y:
                not_covered.add((x, y))
                if i > 0:
                    not_covered.add((sorted_buildings_by_y[i - 1][0], sorted_buildings_by_y[i - 1][1]))
            prev_y = y
        not_covered.add((sorted_buildings_by_y[-1][0], sorted_buildings_by_y[-1][1]))
        
        return len(buildings) - len(not_covered)