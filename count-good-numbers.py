def countGoodNumbers(n):
    if n == 0:
        return 0
    if n == 1:
        return 5
    
    maxLimit = 10 ** 9 + 7
    
    odds = n // 2
    evens = n - odds

    return pow(5, evens, maxLimit) * pow(4, odds, maxLimit) % maxLimit