class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10 ** 9 + 7
        total = [[0] * n for _ in range(m)]
        dp_right = [[0] * n for _ in range(m)]
        dp_down = [[0] * n for _ in range(m)]
        total[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                if grid[i][j - 1] == 0:
                    dp_right[i][j] = total[i][j - 1]
                else:
                    dp_right[i][j] = dp_down[i][j - 1]

                if grid[i - 1][j] == 0:
                    dp_down[i][j] = total[i - 1][j]
                else:
                    dp_down[i][j] = dp_right[i - 1][j]

                if grid[i][j] == 0:
                    total[i][j] = (dp_right[i][j] + dp_down[i][j]) % MOD

        return total[m - 1][n - 1]