# B. Special Permutation
# time limit per test2 seconds
# memory limit per test512 megabytes
# A permutation of length n
#  is an array p=[p1,p2,…,pn]
#  which contains every integer from 1
#  to n
#  (inclusive) exactly once. For example, p=[4,2,6,5,3,1]
#  is a permutation of length 6
# .

# You are given three integers n
# , a
#  and b
# , where n
#  is an even number. Print any permutation of length n
#  that the minimum among all its elements of the left half equals a
#  and the maximum among all its elements of the right half equals b
# . Print -1 if no such permutation exists.

# Input
# The first line of the input contains one integer t
#  (1≤t≤1000
# ), the number of test cases in the test. The following t
#  lines contain test case descriptions.

# Each test case description contains three integers n
# , a
# , b
#  (2≤n≤100
# ; 1≤a,b≤n
# ; a≠b
# ), where n
#  is an even number (i.e. nmod2=0
# ).

# Output
# For each test case, print a single line containing any suitable permutation. Print -1 no such permutation exists. If there are multiple answers, print any of them.

# Example
# InputCopy
# 7
# 6 2 5
# 6 1 3
# 6 4 3
# 4 2 4
# 10 5 3
# 2 1 2
# 2 2 1
# OutputCopy
# 4 2 6 5 3 1
# -1
# 6 4 5 1 3 2 
# 3 2 4 1 
# -1
# 1 2 
# 2 1 

import sys

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n, a, b = map(int, input().split())
    
    m = n // 2
    if  a > m + 1 or b < m:
        output.append('-1')
        continue
    
    left = [str(a)]
    i = n 
    while len(left) < m:
        if i == b:
            i -= 1
            continue
        left.append(str(i))
        i -= 1
        
    right = [str(b)]
    for i in range(1, b):
        if str(i) not in left:
            right.append(str(i))
            
    if len(left) == len(right) == m:
        output.append(' '.join(left + right))
    else:
        output.append('-1')
        
print('\n'.join(output))