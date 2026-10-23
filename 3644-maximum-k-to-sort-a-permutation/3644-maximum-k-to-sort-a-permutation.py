class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        arr = []
        for i, num in enumerate(nums):
            if i != num:
                arr.append(num)

        return reduce(and_, arr) if arr else 0