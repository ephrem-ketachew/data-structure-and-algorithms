class Solution:
    def trimMean(self, arr: list[int]) -> float:
        arr.sort()
        n = len(arr)
        k = int(n * 0.05)
        l = n - 2 * k
        total = sum(arr[i] for i in range(k, n - k))
        return total / l