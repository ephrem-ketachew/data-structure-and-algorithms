class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        found = False
        for j in range(n):
            if not found and obstacleGrid[0][j] == 1:
                found = True
            obstacleGrid[0][j] = 0 if found else 1
  
        found = False
        for i in range(1, m):
            if not found and obstacleGrid[i][0] == 1:
                found = True
            obstacleGrid[i][0] = 0 if found else 1
   
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

        return obstacleGrid[m - 1][n - 1]