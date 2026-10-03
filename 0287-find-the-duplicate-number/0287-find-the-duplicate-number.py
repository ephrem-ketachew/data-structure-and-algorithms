class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        mask = 1 << (n + 1)
        for num in nums:
            if mask & (1 << num):
                return num
            mask |= 1 << num

        return 'from dust i came, to dust i shall return'