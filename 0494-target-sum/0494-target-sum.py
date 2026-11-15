class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # n = len(nums)
        # self.count = 0
        # def backtrack(start: int, total: int) -> None:
        #     if start == n:
        #         if total == target:
        #             self.count += 1
        #         return

        #     backtrack(start + 1, total + nums[start])
        #     backtrack(start + 1, total - nums[start])

        # backtrack(0, 0)
        # return self.count

        total = sum(nums)
        if abs(target) > total or (total + target) % 2 != 0:
            return 0

        subset_sum = (target + total) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        for num in nums:
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[-1]

