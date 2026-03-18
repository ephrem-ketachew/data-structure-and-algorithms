# D. Parity Sort
# time limit per test2 seconds
# memory limit per test256 megabytes
# You have an array of integers a
#  of length n
# . You can apply the following operation to the given array:

# Swap two elements ai
#  and aj
#  such that i≠j
# , ai
#  and aj
#  are either both even or both odd.
# Determine whether it is possible to sort the array in non-decreasing order by performing the operation any number of times (possibly zero).

# For example, let a
#  = [7,10,1,3,2
# ]. Then we can perform 3
#  operations to sort the array:

# Swap a3=1
#  and a1=7
# , since 1
#  and 7
#  are odd. We get a
#  = [1,10,7,3,2
# ];
# Swap a2=10
#  and a5=2
# , since 10
#  and 2
#  are even. We get a
#  = [1,2,7,3,10
# ];
# Swap a4=3
#  and a3=7
# , since 3
#  and 7
#  are odd. We get a
#  = [1,2,3,7,10
# ].
# Input
# The first line of input data contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.

# The description of the test cases follows.

# The first line of each test case contains one integer n
#  (1≤n≤2⋅105
# ) — the length of array a
# .

# The second line of each test case contains exactly n
#  positive integers a1,a2,…,an
#  (1≤ai≤109
# ) — the elements of array a
# .

# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .

# Output
# For each test case, output on a separate line:

# YES if the array can be sorted by applying the operation to it some number of times;
# NO otherwise.
# You can output YES and NO in any case (for example, strings yEs, yes, Yes and YES will be recognized as positive response).

# Example
# InputCopy
# 6
# 5
# 7 10 1 3 2
# 4
# 11 9 3 5
# 5
# 11 3 15 3 2
# 6
# 10 7 8 1 2 3
# 1
# 10
# 5
# 6 6 4 1 6
# OutputCopy
# YES
# YES
# NO
# NO
# YES
# NO
# Note
# The first test case is explained in the problem statement.

import sys

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    odds = []
    evens = []
    for num in arr:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
     
    odds.sort()
    evens.sort()
    
    is_possible = True       
    m, n = len(odds), len(evens)
    i = j = 0
    for num in arr:
        if num % 2 == 1:
            if i == m or (j < n and odds[i] > evens[j]):
                is_possible = False
                break
            i += 1
        else:
            if j == n or (i < m and odds[i] < evens[j]):
                is_possible = False
                break
            j += 1
    
    if is_possible:
        output.append('YES')
    else:
        output.append('NO')
        
print('\n'.join(output))