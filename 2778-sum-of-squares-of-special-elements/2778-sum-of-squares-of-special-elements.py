class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        summ, n = 0, len(nums)
        for i, num in enumerate(nums, start=1):
            if n % i == 0:
                summ += num ** 2
                
        return summ