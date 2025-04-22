def maxProfit(prices):
    # Brute force : time limit exceeded
    # profit = 0
    # for i in range(len(prices) - 1):
    #     for j in range(i + 1, len(prices)):
    #         if prices[j] - prices[i] > profit:
    #             profit = prices[j] - prices[i]
    # return profit

    minPrice = float('inf')
    maxProfit = 0
    for i in range(len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        elif prices[i] - minPrice > maxProfit:
            maxProfit = prices[i] - minPrice
    return maxProfit