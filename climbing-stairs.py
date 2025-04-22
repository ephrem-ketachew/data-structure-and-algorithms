def climbStairs(n):
    if n == 1 or n == 2:
        return n
    
    first = 1
    second = 2

    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third
    
    return second


# def climbStairs(n):
#     if n == 1 or n == 2:
#         return n
#     return climbStairs(n-1) + climbStairs(n-2)
