def hammingWeight(n):
    numberOfSetBits = 0
    while n > 0:
        digit = n % 2
        if digit == 1:
            numberOfSetBits += 1
        n //= 2
    return numberOfSetBits