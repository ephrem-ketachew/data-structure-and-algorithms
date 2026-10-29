class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return min(matrix[0])
            
        prev_min = matrix[0][:]
        for i in range(1, n):
            cur_min = [float('inf')] * n
            for j in range(n):
                cur_min[j] = min(cur_min[j], matrix[i][j] + prev_min[j])
                if j - 1 >= 0:
                    cur_min[j] = min(cur_min[j], matrix[i][j] + prev_min[j - 1])
                if j + 1 < n:
                    cur_min[j] = min(cur_min[j], matrix[i][j] + prev_min[j + 1])

            prev_min = cur_min

        return min(cur_min)