class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            uniques = set()
            for j in range(i, n):
                uniques.add(nums[j])
                total += len(uniques) * len(uniques)
                
        return total