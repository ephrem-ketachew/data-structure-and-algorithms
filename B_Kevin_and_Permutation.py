# B. Kevin and Permutation
# time limit per test1 second
# memory limit per test256 megabytes

# Kevin is a master of permutation-related problems. You are taking a walk with Kevin in Darkwoods, and during your leisure time, he wants to ask you the following question.

# Given two positive integers n
#  and k
# , construct a permutation∗
#  p
#  of length n
#  to minimize the sum of the minimum values of all subarrays†
#  of length k
# . Formally, you need to minimize

# ∑i=1n−k+1(minj=ii+k−1pj).

# ∗
# A permutation of length n
#  is an array consisting of n
#  distinct integers from 1
#  to n
#  in arbitrary order. For example, [2,3,1,5,4]
#  is a permutation, but [1,2,2]
#  is not a permutation (2
#  appears twice in the array), and [1,3,4]
#  is also not a permutation (n=3
#  but there is 4
#  in the array).

# †
# An array a
#  is a subarray of an array b
#  if a
#  can be obtained from b
#  by the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end. Two subarrays are considered different if the sets of positions of the deleted elements are different.

# Input
# Each test consists of multiple test cases. The first line contains the number of test cases t
#  (1≤t≤103
# ).

# The only line of each test case contains two integers n
#  and k
#  (1≤k≤n≤105
# ).

# It is guaranteed that the sum of n
#  over all test cases doesn't exceed 105
# .

# Output
# For each test case, output n
#  integers on a single line — the permutation p
#  you constructed.

# If there are multiple answers, you can print any of them.

# Example
# InputCopy
# 3
# 4 2
# 6 1
# 8 3
# OutputCopy
# 3 1 2 4
# 5 2 1 6 4 3
# 4 6 2 8 3 1 5 7
# Note
# In the first test case, with k=2
# , consider all subarrays of length 2
# : the minimum value of p1,p2
#  is 1
# , the minimum value of p2,p3
#  is 1
# , and the minimum value of p3,p4
#  is 2
# . The sum 1+1+2=4
#  is the smallest among all possible permutations.

# In the second test case, all subarrays of length 1
#  have minimum values of 5,2,1,6,4,3
# , and the sum 5+2+1+6+4+3=21
#  is proven to be the smallest.

import sys

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n, k = map(int, input().split())
    
    arr = [0] * n
    i = k - 1
    start = 1
    while i < n:
        arr[i] = str(start)
        start += 1
        i += k
    
    i = 0    
    while start <= n:
        if (i + 1) % k != 0:
            arr[i] = str(start)
            start += 1
        i += 1
        
    output.append(' '.join(arr))
    
print('\n'.join(output))