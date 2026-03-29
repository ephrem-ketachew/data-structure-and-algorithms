# B. BAN BAN
# time limit per test1 second
# memory limit per test256 megabytes
# You are given an integer n
# .

# Let's define s(n)
#  as the string "BAN" concatenated n
#  times. For example, s(1)
#  = "BAN", s(3)
#  = "BANBANBAN". Note that the length of the string s(n)
#  is equal to 3n
# .

# Consider s(n)
# . You can perform the following operation on s(n)
#  any number of times (possibly zero):

# Select any two distinct indices i
#  and j
#  (1≤i,j≤3n,i≠j)
# .
# Then, swap s(n)i
#  and s(n)j
# .
# You want the string "BAN" to not appear in s(n)
#  as a subsequence. What's the smallest number of operations you have to do to achieve this? Also, find one such shortest sequence of operations.

# A string a
#  is a subsequence of a string b
#  if a
#  can be obtained from b
#  by deletion of several (possibly, zero or all) characters.

# Input
# The input consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤100)
#   — the number of test cases. The description of the test cases follows.

# The only line of each test case contains a single integer n
#  (1≤n≤100)
# .

# Output
# For each test case, in the first line output m
#  (0≤m≤105
# ) — the minimum number of operations required. It's guaranteed that the objective is always achievable in at most 105
#  operations under the constraints of the problem.

# Then, output m
#  lines. The k
# -th of these lines should contain two integers ik
# , jk
#  (1≤ik,jk≤3n,ik≠jk)
#  denoting that you want to swap characters at indices ik
#  and jk
#  at the k
# -th operation.

# After all m
#  operations, "BAN" must not appear in s(n)
#  as a subsequence.

# If there are multiple possible answers, output any.

# Example
# InputCopy
# 2
# 1
# 2
# OutputCopy
# 1
# 1 2
# 1
# 2 6
# Note
# In the first testcase, s(1)=
#  "BAN", we can swap s(1)1
#  and s(1)2
# , converting s(1)
#  to "ABN", which does not contain "BAN" as a subsequence.

# In the second testcase, s(2)=
#  "BANBAN", we can swap s(2)2
#  and s(2)6
# , converting s(2)
#  to "BNNBAA", which does not contain "BAN" as a subsequence.

import sys

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n = int(input())
    
    s = ['B', 'A', 'N'] * n
    swap_count = 0
    swap_indices = []
    left, right = 0, 3 * n - 1
    while left < right:
        if s[left] == 'A':
            if s[right] == 'N':
                swap_count += 1
                swap_indices.append(f'{left + 1} {right + 1}')
                
                left += 1
                right -= 1
            else:
                right -= 1
        else:
            left += 1
            
    output.append(str(swap_count))
    output.extend(swap_indices)
    
print('\n'.join(output))