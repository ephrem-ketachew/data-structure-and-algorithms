class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        free = [0] * n
        for i in range(n):
            factori, _ = items[i]
            for j in range(n):
                factorj, _ = items[j]
                if i != j and factorj % factori == 0:
                    free[i] += 1

        dp = [0] * (budget + 1)
        for i in range(n):
            _, price = items[i]
            value = free[i] + 1
            for t in range(budget, price - 1, -1):
                dp[t] = max(dp[t], dp[t - price] + value)

        min_price = min(price for _, price in items)
        for p in range(min_price, budget + 1):
            dp[p] = max(dp[p], dp[p - min_price] + 1)

        return dp[budget]