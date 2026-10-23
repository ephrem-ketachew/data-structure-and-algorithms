class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = float('inf')
        idx_map = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            if num != i:
                idx = idx_map[i]
                if k != float('inf'):
                    k = k & num & nums[idx]
                else:
                    k = num & nums[idx]
                nums[i], nums[idx] = nums[idx], nums[i]
                idx_map[i] = i
                idx_map[num] = idx

        return k if k != float('inf') else 0