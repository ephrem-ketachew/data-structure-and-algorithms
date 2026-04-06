# B. Array
# time limit per test1.5 seconds
# memory limit per test256 megabytes

# You are given an integer array a
#  of length n
# .

# For each index i
# , find the maximum number of indices j
#  such that j>i
#  and |ai−k|>|aj−k|
# , over all possible integer values of k
# .

# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤100
# ). The description of the test cases follows.

# The first line of each test case contains an integer n
#  (1≤n≤5000
# ).

# The second line contains n
#  integers a1,a2,…,an
#  (−109≤ai≤109
# ).

# It is guaranteed that the sum of n
#  over all test cases does not exceed 5000
# .

# Output
# For each test case, output n
#  integers denoting the answer.

# Example
# InputCopy
# 6
# 1
# 1092
# 2
# 105 -105
# 5
# 1 2 93 84 2
# 7
# 2 9 38 4 7 1 6
# 10
# 1 9 20 9 829 3 87 1 283 7
# 11
# 9 18 29817 283 3 3928 5726 1942 1000000000 -1000000000 19
# OutputCopy
# 0
# 1 0
# 4 2 2 1 0
# 5 4 4 2 2 1 0
# 8 4 4 3 5 3 2 2 1 0
# 8 7 7 4 5 3 3 2 2 1 0
# Note
# In the second test, the answers are:

# For i=1
# , you can choose k=−195
# , then j=2
# .
# For i=2
# , you can choose k=5
# , there exists no index j>i
# .
# In the third test, the answers are:

# For i=1
# , you can choose k=195
# , then j=2,3,4,5
# .
# For i=2
# , you can choose k=78
# , then j=3,4
# .
# For i=3
# , you can choose k=15
# , then j=4,5
# .
# For i=4
# , you can choose k=15
# , then j=5
# .
# For i=5
# , you can choose k=998244353
# , there exists no index j>i
# .

import sys

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = ['0'] * n
    for i in range(n - 1):
        less_count = greater_count = 0
        for j in range(i + 1, n):
            if a[j] > a[i]:
                greater_count += 1
            elif a[j] < a[i]:
                less_count += 1
                
        ans[i] = str(max(less_count, greater_count))
        
    output.append(' '.join(ans))
    
print('\n'.join(output))