# C. Gorilla and Permutation
# time limit per test2 seconds
# memory limit per test256 megabytes
# Gorilla and Noobish_Monk found three numbers n
# , m
# , and k
#  (m<k
# ). They decided to construct a permutation†
#  of length n
# .

# For the permutation, Noobish_Monk came up with the following function: g(i)
#  is the sum of all the numbers in the permutation on a prefix of length i
#  that are not greater than m
# . Similarly, Gorilla came up with the function f
# , where f(i)
#  is the sum of all the numbers in the permutation on a prefix of length i
#  that are not less than k
# . A prefix of length i
#  is a subarray consisting of the first i
#  elements of the original array.

# For example, if n=5
# , m=2
# , k=5
# , and the permutation is [5,3,4,1,2]
# , then:

# f(1)=5
# , because 5≥5
# ; g(1)=0
# , because 5>2
# ;
# f(2)=5
# , because 3<5
# ; g(2)=0
# , because 3>2
# ;
# f(3)=5
# , because 4<5
# ; g(3)=0
# , because 4>2
# ;
# f(4)=5
# , because 1<5
# ; g(4)=1
# , because 1≤2
# ;
# f(5)=5
# , because 2<5
# ; g(5)=1+2=3
# , because 2≤2
# .
# Help them find a permutation for which the value of (∑ni=1f(i)−∑ni=1g(i))
#  is maximized.

# †
# A permutation of length n
#  is an array consisting of n
#  distinct integers from 1
#  to n
#  in any order. For example, [2,3,1,5,4]
#  is a permutation, but [1,2,2]
#  is not a permutation (as 2
#  appears twice in the array) and [1,3,4]
#  is also not a permutation (as n=3
# , but 4
#  appears in the array).

# Input
# The first line contains a single integer t
#  (1≤t≤104
# )  — the number of test cases.

# The only line of each case contains three integers n
# , m
# , k
#  (2≤n≤105
# ; 1≤m<k≤n
# ) — the size of the permutation to be constructed and two integers.

# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .

# Output
# For each test case, output the permutation  — a set of numbers that satisfies the conditions of the problem. If there are multiple solutions, output any of them.

# Example
# InputCopy
# 3
# 5 2 5
# 3 1 3
# 10 3 8
# OutputCopy
# 5 3 4 1 2
# 3 2 1
# 10 9 8 4 7 5 6 1 2 3
# Note
# In the first example, (∑ni=1f(i)−∑ni=1g(i))=5⋅5−(0⋅3+1+3)=25−4=21

import sys

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n, m, k = map(int, input().split())
    
    arr = []
    for i in range(n, 0, -1):
        arr.append(str(i))
     
    p = n - k + 1   
    q = min(n - p, m)
    
    arr[-q:] = arr[-q:][::-1]
        
    output.append(' '.join(arr))
    
print('\n'.join(output))    
    