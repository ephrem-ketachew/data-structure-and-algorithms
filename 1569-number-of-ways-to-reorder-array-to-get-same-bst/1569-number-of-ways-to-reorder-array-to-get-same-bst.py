class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7
        def dfs(nums):
            if len(nums) < 3:
                return 1

            left_nodes = [num for num in nums if num < nums[0]]
            right_nodes = [num for num in nums if num > nums[0]]
            return dfs(left_nodes) * dfs(right_nodes) * comb(len(nums) - 1, len(left_nodes)) % MOD

        return dfs(nums) - 1