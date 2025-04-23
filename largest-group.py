def countLargestGroup(n):
    groups = {}
    def sumOfDigits(num):
        result = 0
        while num > 0:
            result += num % 10
            num //= 10
        return result
    
    for i in range(1, n + 1):
        s = sumOfDigits(i)
        groups[s] = groups.get(s, 0) + 1
    
    
    maxValue = max(groups.values())

    return sum(1 for qunatity in groups.values() if qunatity == maxValue)
