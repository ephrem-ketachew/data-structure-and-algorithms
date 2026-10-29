class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1
        for i, num in enumerate(nums):
            if i != num:
                k &= i

        return k if k != -1 else 0