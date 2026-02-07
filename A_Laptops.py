# A. Laptops
# time limit per test1 second
# memory limit per test256 megabytes
# One day Dima and Alex had an argument about the price and quality of laptops. Dima thinks that the more expensive a laptop is, the better it is. Alex disagrees. Alex thinks that there are two laptops, such that the price of the first laptop is less (strictly smaller) than the price of the second laptop but the quality of the first laptop is higher (strictly greater) than the quality of the second laptop.

# Please, check the guess of Alex. You are given descriptions of n laptops. Determine whether two described above laptops exist.

# Input
# The first line contains an integer n (1 ≤ n ≤ 105) — the number of laptops.

# Next n lines contain two integers each, ai and bi (1 ≤ ai, bi ≤ n), where ai is the price of the i-th laptop, and bi is the number that represents the quality of the i-th laptop (the larger the number is, the higher is the quality).

# All ai are distinct. All bi are distinct.

# Output
# If Alex is correct, print "Happy Alex", otherwise print "Poor Alex" (without the quotes).

# Examples
# InputCopy
# 2
# 1 2
# 2 1
# OutputCopy
# Happy Alex

n = int(input())

arr = []
for _ in range(n):
    price, quality = map(int, input().split())
    arr.append([price, quality])
    
arr.sort()
price_of_max, max_quality_seen = arr[0]
for price, quality in arr:
    if quality < max_quality_seen and price > price_of_max:
        print('Happy Alex')
        break
    if quality > max_quality_seen:
        max_quality_seen = quality
        price_of_max = price
else:
    print('Poor Alex')