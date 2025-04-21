def mySqrt(x):
    for i in range(x+1):
        if i * i == x:
            return i
        if i * i > x:
            return i - 1
        
print(mySqrt(24))