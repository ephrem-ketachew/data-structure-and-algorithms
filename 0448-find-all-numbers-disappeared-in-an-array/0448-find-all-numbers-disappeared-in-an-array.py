class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for i, num in enumerate(nums):
            nums[abs(nums[i]) - 1] = abs(nums[abs(nums[i]) - 1]) * -1

        ans = []
        for i, num in enumerate(nums):
            if num > 0:
                ans.append(i + 1)

        return ans