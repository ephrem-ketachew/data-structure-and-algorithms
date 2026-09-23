class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if nums[0] == 0 and len(nums) > 1:
            return False

        max_jump_idx = 0
        for i, num in enumerate(nums):
            if i > max_jump_idx:
                return False
            max_jump_idx = max(max_jump_idx, i + num)
            if max_jump_idx >= len(nums) - 1:
                return True

        return True

        