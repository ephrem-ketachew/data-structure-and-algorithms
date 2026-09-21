class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prev = 0
        cost = [0] * n
        for j in range(n):
            prev += grid[0][j]
            cost[j] = prev

        prev = cost[0]
        for i in range(1, m):
            prev += grid[i][0]
            cost[0] = prev
            curr = prev
            for j in range(1, n):
                curr = grid[i][j] + min(curr, cost[j])
                cost[j] = curr

        return cost[-1]


