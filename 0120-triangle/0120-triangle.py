class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        dp_cur = [triangle[0][0]]
        for i in range(1, len(triangle)):
            dp_prev = dp_cur
            dp_cur = triangle[i][:]
            for j in range(len(dp_cur)):
                if j == 0:
                    dp_cur[j] += dp_prev[j]
                elif j == len(dp_cur) - 1:
                    dp_cur[j] += dp_prev[j - 1]
                else:
                    dp_cur[j] += min(dp_prev[j - 1], dp_prev[j])

        return min(dp_cur)