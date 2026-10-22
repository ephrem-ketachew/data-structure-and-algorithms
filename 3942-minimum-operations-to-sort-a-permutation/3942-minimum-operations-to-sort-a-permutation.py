class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        idx = nums.index(0)
        forward = backward = True
        for i in range(idx, idx + n - 1):
            if nums[(i + 1) % n] != nums[i % n] + 1:
                forward = False
                break

        for i in range(idx, idx - n + 1, -1):
            if nums[(i + n - 1) % n] != nums[(i + n) % n] + 1:
                backward = False
                break

        if not (forward or backward):
            return -1

        if forward:
            return min(idx, n - idx + 2)

        if nums[-1] == 0:
            return 1

        return min(idx + 2, n - idx)