# B. XOR = Average
# time limit per test1 second
# memory limit per test256 megabytes
# You are given an integer n
# . Find a sequence of n
#  integers a1,a2,…,an
#  such that 1≤ai≤109
#  for all i
#  and
# a1⊕a2⊕⋯⊕an=a1+a2+⋯+ann,
# where ⊕
#  represents the bitwise XOR.

# It can be proven that there exists a sequence of integers that satisfies all the conditions above.

# Input
# The first line of input contains t
#  (1≤t≤104
# ) — the number of test cases.

# The first and only line of each test case contains one integer n
#  (1≤n≤105
# ) — the length of the sequence you have to find.

# The sum of n
#  over all test cases does not exceed 105
# .

# Output
# For each test case, output n
#  space-separated integers a1,a2,…,an
#  satisfying the conditions in the statement.

# If there are several possible answers, you can output any of them.

# Example
# InputCopy
# 3
# 1
# 4
# 3
# OutputCopy
# 69
# 13 2 8 1
# 7 7 7
# Note
# In the first test case, 69=691=69
# .

# In the second test case, 13⊕2⊕8⊕1=13+2+8+14=6
# .

import sys

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n = int(input())
    
    if n % 2 == 1:
        output.append(' '.join(['1'] * n))
    else:
        output.append(' '.join(['2'] * (n - 2) + ['1', '3']))
        
print('\n'.join(output))
