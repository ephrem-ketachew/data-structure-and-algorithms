class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # grid = [[1] * n for _ in range(m)]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         grid[i][j] = grid[i][j - 1] + grid[i - 1][j]

        # return grid[m - 1][n - 1]

        row = [1] * n
        for i in range(1, m):
            curr = 1
            for j in range(1, n):
                curr += row[j]
                row[j] = curr

        return row[-1]

