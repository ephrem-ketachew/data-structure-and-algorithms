class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for x in range(2, n + 1):
            for i in range(1, x):
                left_over = x - i
                break_it = i * left_over
                dont_break = i * dp[left_over]

                dp[x] = max(dp[x], break_it, dont_break)

        return dp[n]