# 864. Shortest Path to Get All Keys
# Hard

# You are given an m x n grid grid where:

# '.' is an empty cell.
# '#' is a wall.
# '@' is the starting point.
# Lowercase letters represent keys.
# Uppercase letters represent locks.
# You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

# If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

# For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

# Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

# Example 1:

# Input: grid = ["@.a..","###.#","b.A.B"]
# Output: 8
# Explanation: Note that the goal is to obtain all the keys not to open all the locks.
# Example 2:

# Input: grid = ["@..aA","..B#.","....b"]
# Output: 6
# Example 3:

# Input: grid = ["@Aa"]
# Output: -1

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 30
# grid[i][j] is either an English letter, '.', '#', or '@'. 
# There is exactly one '@' in the grid.
# The number of keys in the grid is in the range [1, 6].
# Each key in the grid is unique.
# Each key in the grid has a matching lock.

from typing import List
from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        keys_count = 0
        start_x, start_y = -1, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start_x, start_y = i, j
                elif grid[i][j].islower():
                    keys_count += 1
        
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]           
        target_mask = (1 << keys_count) - 1
        visited = set([(start_x, start_y, 0)])
        dq = deque([start_x, start_y, 0, 0])
        while dq:
            r, c, mask, steps = dq.popleft()
            if mask == target_mask:
                return steps
            
            for dr, dc in moves:
                x, y = r + dr, c + dc
                if 0 <= x < m and 0 <= y < n and grid[x][y] != '#':
                    new_mask = mask
                    if grid[x][y].isupper():
                        req_key_bit = ord(grid[x][y].lower()) - ord('a')
                        if not (new_mask & (1 << req_key_bit)):
                            continue
                        
                    elif grid[x][y].islower():
                        key_bit = ord(grid[x][y]) - ord('a')
                        new_mask = new_mask | (1 << key_bit)
                        
                    if (x, y, new_mask) not in visited:
                        visited.add((x, y, new_mask))
                        dq.append((x, y, new_mask, steps + 1))
                        
        return -1