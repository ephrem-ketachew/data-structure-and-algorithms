class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # if nums[0] == 0 and len(nums) > 1:
        #     return False

        # max_jump_idx = 0
        # for i, num in enumerate(nums):
        #     if i > max_jump_idx:
        #         return False
        #     max_jump_idx = max(max_jump_idx, i + num)
        #     if max_jump_idx >= len(nums) - 1:
        #         return True

        # return True

        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        for i in range(n - 2, -1, -1):
            farthest_jump = min(i + nums[i], n - 1)
            for j in range(i + 1, farthest_jump + 1):
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0]



        