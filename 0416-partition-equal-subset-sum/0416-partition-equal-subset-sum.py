class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for t in range(target, num - 1, -1):
                if dp[t - num]:
                    dp[t] = True

        return dp[-1]