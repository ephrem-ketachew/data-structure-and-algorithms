class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        min_jumps = [float('inf')] * n
        min_jumps[0] = 0
        for i, num in enumerate(nums):
            max_jump = min(i + num, n - 1)
            for j in range(i + 1, max_jump + 1):
                min_jumps[j] = min(min_jumps[j], min_jumps[i] + 1)

        return min_jumps[-1]