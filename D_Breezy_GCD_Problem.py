# D. Breezy GCD Problem
# time limit per test1 second
# memory limit per test256 megabytes
# You are given n
#  intervals [li,ri]
# , where li≤ri
# . Your task is to determine if there exist n
#  integers x1,x2,…,xn
#  satisfying:

# li≤xi≤ri
#  for all 1≤i≤n
# ;
# gcd(x1,x2,…,xn)≠1
# .
# Here, gcd(x1,x2,…,xn)
#  denotes the greatest common divisor of x1,x2,…,xn
# .
# Input
# The first line contains an integer t
#  (1≤t≤104
# ), the number of test cases.

# For each test case:

# The first line contains an integer n
#  (2≤n≤105
# ) denoting the number of intervals.
# The second line contains n
#  integers l1,l2,…,ln
#  (1≤li≤106
# ).
# The third line contains n
#  integers r1,r2,…,rn
#  (li≤ri≤106
# ).
# It is guaranteed that the sum of n
#  over all test cases does not exceed 105
# .

# Output
# For each test case, output:

# YES if it is possible to choose x1,x2,…,xn
#  such that it satisfies the constraints. On the next line, output n
#  space-separated integers x1,x2,…,xn
# .
# NO otherwise.
# The letters in the word YES and NO are case insensitive. For example, YES, yeS and No are all considered valid.

# Example
# InputCopy
# 4
# 3
# 1 5 10
# 5 6 11
# 4
# 2 3 4 1000000
# 2 3 4 1000000
# 5
# 34 15 55 233 51
# 34 20 99 299 51
# 3
# 1 1 1
# 1 1 2
# OutputCopy
# YES
# 5 5 10
# NO
# YES
# 34 17 85 255 51
# NO
# Note
# In the first example, we choose 5
# , 5
#  and 10
#  respectively from each range. Then, we have gcd(5,5,10)=5≠1
# .

# In the second example, it is not possible to choose n
#  integers satisfying the condition.


import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    
    fixed_idx = -1
    for i in range(n):
        if l[i] == r[i]:
            fixed_idx = i
            break
        
    if fixed_idx == -1:
        print('YES')
        ans = [l[i] if l[i] % 2 == 0 else l[i] + 1 for i in range(n)]
        print(*ans)
        continue
    
    if l[fixed_idx] == 1:
        print('NO')
        continue
    
    value = l[fixed_idx]
    primes = []
    temp = value
    d = 2
    while d * d <= temp:
        if temp % d == 0:
            primes.append(d)
            while temp % d == 0:
                temp //= d 
        d += 1
        
    if temp > 1:
        primes.append(temp)
        
    found_valid = False
    for p in primes:
        ans = []
        valid = True
        for i in range(n):
            val = ((l[i] + p - 1) // p) * p
            if val <= r[i]:
                ans.append(val)
            else:
                valid = False
        
        if valid:
            found_valid = True
            print('YES')
            print(*ans)
            break
            
    if not found_valid:
        print('NO')