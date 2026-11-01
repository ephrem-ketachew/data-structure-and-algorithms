class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_el = min(nums)
        count = 0
        for num in nums:
            count += num - min_el
            
        return count