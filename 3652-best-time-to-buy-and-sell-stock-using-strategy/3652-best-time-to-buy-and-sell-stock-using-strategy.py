class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + prices[i] * strategy[i]

        profit = sum(prices[i] * strategy[i] for i in range(n))
        window = sum(prices[i] for i in range(k//2, k))
        max_profit = max(profit, prefix[n] - prefix[k] + window)
        for i in range(k, n):
            window += prices[i] - prices[i - k // 2]
            profit = prefix[n] - prefix[i + 1] + prefix[i - k + 1] + window
            max_profit = max(max_profit, profit)

        return max_profit