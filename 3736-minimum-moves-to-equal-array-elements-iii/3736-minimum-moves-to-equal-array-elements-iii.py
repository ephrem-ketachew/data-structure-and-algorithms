class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_el = max(nums)
        return sum(max_el - num for num in nums)