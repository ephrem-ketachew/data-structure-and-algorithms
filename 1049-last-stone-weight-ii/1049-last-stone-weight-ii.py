class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for stone in stones:
            for t in range(target, stone - 1, -1):
                if dp[t - stone]:
                    dp[t] = True
        
        max_balanced_half = 0
        for i in range(target, -1, -1):
            if dp[i]:
                max_balanced_half = i
                break

        return total - (2 * max_balanced_half)