class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True, key=abs)
        res = 0
        for i in range((n + 1) // 2):
            res += nums[i] * nums[i]

        for i in range((n + 1) // 2, n):
            res -= nums[i] * nums[i]

        return res