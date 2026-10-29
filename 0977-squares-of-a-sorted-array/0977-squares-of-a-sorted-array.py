class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        pivot = len(nums)
        for i, num in enumerate(nums):
            if num >= 0:
                pivot = i
                break

        left, right = pivot - 1, pivot
        ans = []
        while left >= 0 and right < len(nums):
            if abs(nums[left]) <= nums[right]:
                ans.append(nums[left] ** 2)
                left -= 1
            else:
                ans.append(nums[right] ** 2)
                right += 1

        while left >= 0:
            ans.append(nums[left] ** 2)
            left -= 1

        while right < len(nums):
            ans.append(nums[right] ** 2)
            right += 1

        return ans

