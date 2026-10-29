class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        uniques = list(set(nums))
        uniques.sort(key=lambda x: counter[x], reverse=True)
        return uniques[:k]