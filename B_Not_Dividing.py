# B. Not Dividing
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given an array of n
#  positive integers a1,a2,…,an
# . In one operation, you can choose any number of the array and add 1
#  to it.

# Make at most 2n
#  operations so that the array satisfies the following property: ai+1
#  is not divisible by ai
# , for each i=1,2,…,n−1
# .

# You do not need to minimize the number of operations.

# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.

# The first line of each test case contains an integer n
#  (1≤n≤104
# ) — the length of the given array.

# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ) — the given array.

# It is guaranteed that the sum of n
#  over all test cases does not exceed 5⋅104
# .

# Output
# For each test case, print the answer on a separate line.

# In the only line, print n
#  integers — the resulting array a
#  after applying at most 2n
#  operations.

# We can show that an answer always exists under the given constraints. If there are multiple answers, print any of them.

# Example
# InputCopy
# 3
# 4
# 2 4 3 6
# 3
# 1 2 3
# 2
# 4 2
# OutputCopy
# 4 5 6 7
# 3 2 3
# 4 2
# Note
# In the first test case, the array [4,5,6,7]
#  can be achieved by applying 2
#  operations to the first element, 1
#  operation to the second element, 3
#  operations to the third element, and 1
#  operation to the last element. The total number of operations performed is 7
# , which is less than the allowed 8
#  operations in this case.

# In the second test case, the array [3,2,3]
#  can be achieved by applying two operations to the first element. Another possible resulting array could be [2,3,5]
# , because the total number of operations does not need to be minimum.

# In the third test case, not applying any operations results in an array that satisfies the statement's property. Observe that it is not mandatory to make operations.


import sys

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        arr[0] += 1
    for i in range(1, n):
        if i - 1 < n and arr[i] == 1:
            arr[i] += 1
        if arr[i] % arr[i - 1] == 0:
            arr[i] += 1
            
    arr = [str(num) for num in arr]
    
    output.append(' '.join(arr))    
    
print('\n'.join(output))    