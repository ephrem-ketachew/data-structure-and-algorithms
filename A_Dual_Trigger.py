# A. Dual Trigger
# time limit per test1 second
# memory limit per test256 megabytes
# Ngọt - LẦN CUỐI (đi bên em xót xa người ơi)
# ඞ
# There are n
#  lamps numbered 1
#  to n
#  lined up in a row, initially turned off. You can perform the following operation any number of times (possibly zero):

# Choose two non-adjacent†
#  lamps that are currently turned off, then turn them on.
# Determine whether you can reach configuration s
# , where si=1
#  means the i
# -th lamp is turned on, and si=0
#  otherwise.

# †
#  Only lamp i
#  and i+1
#  are adjacent for all 1≤i<n
# . Note that lamp n
#  and 1
#  are not adjacent when n≠2
# .

# Input
# Each test contains multiple test cases. The first line contains an integer t
#  (1≤t≤1000
# ) — the number of test cases. The description of the test cases follows.

# The first line of each test case contains an integer n
#  (1≤n≤50
# ) — the number of lamps.

# The second line of each test case contains a binary string s
#  of size n
#  — the final desired configuration.

# Output
# For each test case, print on one line "YES" if we can reach the configuration s
#  via applying the given operation any number of times. Otherwise, print "NO".

# Example
# InputCopy
# 5
# 10
# 1101010110
# 10
# 1001001110
# 6
# 000000
# 1
# 1
# 12
# 111111111111
# OutputCopy
# YES
# NO
# YES
# NO
# YES
# Note
# In the first test case, the sequence of operation could have been as follows (note that initially s
#  is all zero): 0000000000→1000000010→1100000110→1101010110
# .

# In the third test case, we don't have to do any operation.

# In the fourth test case, we cannot do any operation, but we need the first lamp to be on. Therefore, it is impossible to achieve the desired state.

import sys

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n = int(input())
    s = input()
    
    if s.count('1') % 2 == 0:
        output.append('YES')
    else:
        output.append('NO')
        
print('\n'.join(output))