# Q2. Minimum Cost Path with Alternating Directions II
# Medium
# 5 pt.
# You are given two integers m and n representing the number of rows and columns of a grid, respectively.

# The cost to enter cell (i, j) is defined as (i + 1) * (j + 1).

# You are also given a 2D integer array waitCost where waitCost[i][j] defines the cost to wait on that cell.

# You start at cell (0, 0) at second 1.

# At each step, you follow an alternating pattern:

# On odd-numbered seconds, you must move right or down to an adjacent cell, paying its entry cost.
# On even-numbered seconds, you must wait in place, paying waitCost[i][j].
# Return the minimum total cost required to reach (m - 1, n - 1).

# Example 1:

# Input: m = 1, n = 2, waitCost = [[1,2]]

# Output: 3

# Explanation:

# The optimal path is:

# Start at cell (0, 0) at second 1 with entry cost (0 + 1) * (0 + 1) = 1.
# Second 1: Move right to cell (0, 1) with entry cost (0 + 1) * (1 + 1) = 2.
# Thus, the total cost is 1 + 2 = 3.

# Example 2:

# Input: m = 2, n = 2, waitCost = [[3,5],[2,4]]

# Output: 9

# Explanation:

# The optimal path is:

# Start at cell (0, 0) at second 1 with entry cost (0 + 1) * (0 + 1) = 1.
# Second 1: Move down to cell (1, 0) with entry cost (1 + 1) * (0 + 1) = 2.
# Second 2: Wait at cell (1, 0), paying waitCost[1][0] = 2.
# Second 3: Move right to cell (1, 1) with entry cost (1 + 1) * (1 + 1) = 4.
# Thus, the total cost is 1 + 2 + 2 + 4 = 9.

# Example 3:

# Input: m = 2, n = 3, waitCost = [[6,1,4],[3,2,5]]

# Output: 16

# Explanation:

# The optimal path is:

# Start at cell (0, 0) at second 1 with entry cost (0 + 1) * (0 + 1) = 1.
# Second 1: Move right to cell (0, 1) with entry cost (0 + 1) * (1 + 1) = 2.
# Second 2: Wait at cell (0, 1), paying waitCost[0][1] = 1.
# Second 3: Move down to cell (1, 1) with entry cost (1 + 1) * (1 + 1) = 4.
# Second 4: Wait at cell (1, 1), paying waitCost[1][1] = 2.
# Second 5: Move right to cell (1, 2) with entry cost (1 + 1) * (2 + 1) = 6.
# Thus, the total cost is 1 + 2 + 1 + 4 + 2 + 6 = 16.

# Constraints:

# 1 <= m, n <= 105
# 2 <= m * n <= 105
# waitCost.length == m
# waitCost[0].length == n
# 0 <= waitCost[i][j] <= 

from typing import List

class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        # I participated on biweekly leetcode contest and first surprisingly i got easy question and solved and came to this monster........ i thought i could solve it greedily but it turns out the minimum local cost doesn't necessarily lead to the minimum toatl cost ...... and even i heard this question is meant to be solved with  BFS or Dijkstra-like approach🤯....... wait what the fuck even is that thing😅.. lmfao... i damn wasted ah hour trying to solve this greedily... poor me....... and the rest 2 questions were even worse one Dijkstra's algorithm(again) or shortest path search and the last one tagged hard🥵... the heat washed over me and i simply stepped back😅... the title scared me Q4. Minimum Stability Factor of Array©leetcode and the time simply was up
        # i finally ranked 13232 out of 29470 with just 3 points... let this be put for history one day ,I might return and solve it
        
        # take a look at my wrong code if your want to see my effort 
        
        
        
        pass
        # min_cost = 1
        
        # i = j = 0
        
        # while i < n and j < m:
        #     if i + 1 < n:
        #         right_entry_cost = (i + 1 + 1) * (j + 1)
        #         right_wait_cost = waitCost[j][i + 1]
        #         right_cost = right_entry_cost + right_wait_cost
                
        #     if j + 1 < m:
        #         down_entry_cost = (i + 1) * (j + 1 + 1)
        #         down_wait_cost = waitCost[j + 1][i]
        #         down_cost = down_entry_cost + down_wait_cost
            
        #     if j + 1 == m:
        #         if i + 1 != n:
        #             min_cost += right_cost
        #         i += 1
        #     elif i + 1 == n:
        #         if j + 1 != m:
        #             min_cost += down_cost
        #         j += 1
        #     else:                
        #         if right_cost <= down_cost:
        #             if i + 1 != n:
        #                 min_cost += right_cost
        #             i += 1
        #         else: 
        #             if j + 1 != m:
        #                 min_cost += down_cost
        #             j += 1
                
        # return min_cost - waitCost[m-1][n-1]
    
    
# solution = Solution()
# m = 1
# n = 2
# waitCost = [[1,2]]
# m = 2
# n = 2
# waitCost = [[3,5],[2,4]]

# m = 2
# n = 3
# waitCost = [[6,1,4],[3,2,5]]
# print(solution.minCost(m, n, waitCost))