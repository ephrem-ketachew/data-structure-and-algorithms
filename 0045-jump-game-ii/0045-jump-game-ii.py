class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        current = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current:
                current = farthest
                jumps += 1

        return jumps