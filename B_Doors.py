# B. Doors
# time limit per test1 second
# memory limit per test256 megabytes
# There are n
#  doors. You want to open all of them. There are some rules.

# At first, you can only open the first door. For each i≥1
# , you can open the i+1
# -th door only if you have already opened the i
# -th door.

# Initially, you have x
#  coins. There is a lock on the i
# -th door with a cost of ci
# . In other words, you need to spend ci
#  coins to open the i
# -th door. If the number of coins you currently have is strictly less than ci
# , you will not be able to open the i
# -th door. After opening the i
# -th door, you will receive ai
#  coins as a prize.

# You can do the following operation any number of times:

# Choose an index i
# , where 1≤i≤n
# , and set ci
#  to 0
# .
# Find the minimum number of operations necessary to open all the doors.

# Input
# The first line contains an integer t
#  (1≤t≤105
# ), the number of test cases. For each test case:

# The first line contains two integers n
#  and x
#  (1≤n≤2⋅105
# , 1≤x≤109
# ).
# The second line contains n
#  integers c1,c2,…,cn
#  (1≤ci≤109
# ).
# The third line contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ).
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .

# Output
# For each test case, output the minimum number of operations needed to open all the doors.

# Example
# InputCopy
# 3
# 1 1
# 1
# 1
# 3 10
# 9 6 5
# 1 1 1
# 3 10
# 5 9 9
# 1 2 9
# OutputCopy
# 0
# 1
# 2
# Note
# In the first test case, you don't need to perform any operations. You can just spend 1
#  coin to open the first (and only) lock.

# In the second test case, you can first set ci
#  to 0
# . Then, you can do the following:

# Open the first door. You spend 0
#  coins and receive 1
#  coin. After that, you have 11
#  coins.
# Open the second door. You spend 6
#  coins and receive 1
#  coin. After that, you have 6
#  coins.
# Open the third door. You spend 5
#  coins and receive 1
#  coin. After that, you have 2
#  coins.

import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    heap = []
    ops = 0
    for i in range(n):
        heapq.heappush(heap, -c[i])
        x -= c[i]
        
        while x < 0:
            coin = -heapq.heappop(heap)
            x += coin
            ops += 1            
            
        x += a[i]
        
    print(ops)