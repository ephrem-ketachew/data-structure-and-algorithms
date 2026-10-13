class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # n = len(nums)
        # suffix = [1] * (n + 1)
        # pdt = 1
        # for i in range(n - 1, -1, -1):
        #     pdt *= nums[i]
        #     suffix[i] = pdt

        # ans = [1] * n
        # prefix = 1
        # for i in range(n):
        #     ans[i] = prefix * suffix[i + 1]
        #     prefix *= nums[i]

        # return ans

        ans = []
        prefix = 1
        for num in nums:
            ans.append(prefix)
            prefix *= num

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans