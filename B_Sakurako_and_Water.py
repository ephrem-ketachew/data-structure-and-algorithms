# B. Sakurako and Water
# time limit per test2 seconds
# memory limit per test256 megabytes
# During her journey with Kosuke, Sakurako and Kosuke found a valley that can be represented as a matrix of size n×n
# , where at the intersection of the i
# -th row and the j
# -th column is a mountain with a height of ai,j
# . If ai,j<0
# , then there is a lake there.

# Kosuke is very afraid of water, so Sakurako needs to help him:

# With her magic, she can select a square area of mountains and increase the height of each mountain on the main diagonal of that area by exactly one.
# More formally, she can choose a submatrix with the upper left corner located at (i,j)
#  and the lower right corner at (p,q)
# , such that p−i=q−j
# . She can then add one to each element at the intersection of the (i+k)
# -th row and the (j+k)
# -th column, for all k
#  such that 0≤k≤p−i
# .

# Determine the minimum number of times Sakurako must use her magic so that there are no lakes.

# Input
# The first line contains a single integer t
#  (1≤t≤200
# ) — the number of test cases.

# Each test case is described as follows:

# The first line of each test case consists of a single number n
#  (1≤n≤500
# ).
# Each of the following n
#  lines consists of n
#  integers separated by spaces, which correspond to the heights of the mountains in the valley a
#  (−105≤ai,j≤105
# ).
# It is guaranteed that the sum of n
#  across all test cases does not exceed 1000
# .

# Output
# For each test case, output the minimum number of times Sakurako will have to use her magic so that all lakes disappear.

# Example
# InputCopy
# 4
# 1
# 1
# 2
# -1 2
# 3 0
# 3
# 1 2 3
# -2 1 -1
# 0 0 -1
# 5
# 1 1 -1 -1 3
# -3 1 4 4 -4
# -1 -1 3 0 -5
# 4 5 3 -3 -1
# 3 1 -3 -1 5
# OutputCopy
# 0
# 1
# 4
# 19

import sys

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n = int(input())
    
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
        
    count = 0
    for j in range(n):
        minn = 0
        i = 0
        for k in range(n - j):
            minn = min(minn, matrix[i + k][j + k])
                
        if minn < 0:
            count += abs(minn)
            
    for i in range(1, n):
        minn = 0
        j = 0
        for k in range(n - i):
            minn = min(minn, matrix[i + k][j + k])
                
        if minn < 0:
            count += abs(minn)
            
    output.append(str(count))
    
print('\n'.join(output))