# A. Serval and String Theory
# time limit per test1 second
# memory limit per test256 megabytes

# A string r
#  consisting only of lowercase Latin letters is called universal if and only if r
#  is lexicographically smaller∗
#  than the reversal†
#  of r
# .

# You are given a string s
#  consisting of n
#  lowercase Latin letters. You are required to make s
#  universal. To achieve this, you can perform the following operation on s
#  at most k
#  times:

# Choose two indices i
#  and j
#  (1≤i,j≤n
# ), then swap si
#  and sj
# . Note that if i=j
# , you do nothing.
# Determine whether you can make s
#  universal by performing the above operation at most k
#  times.

# ∗
# A string a
#  is lexicographically smaller than a string b
#  of the same length, if and only if the following holds:

# in the first position where a
#  and b
#  differ, the string a
#  has a letter that appears earlier in the alphabet than the corresponding letter in b
# .
# †
# The reversal of a string r
#  is the string obtained by writing r
#  from right to left. For example, the reversal of the string abcad
#  is dacba
# .

# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤500
# ). The description of the test cases follows.

# The first line of each test case contains two integers n
#  and k
#  (1≤n≤100
# , 0≤k≤104
# ) — the length of the string s
# , and the maximum number of operations you can perform.

# The second line contains a string s
#  consisting of n
#  lowercase Latin letters.

# Output
# For each test case, print "YES" if it is possible to make s
#  universal by performing the operation at most k
#  times. Otherwise, print "NO".

# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

# Example
# InputCopy
# 8
# 1 10000
# a
# 3 3
# rev
# 6 0
# string
# 6 0
# theory
# 9 2
# universal
# 19 0
# codeforcesecrofedoc
# 19 1
# codeforcesecrofedoc
# 3 1
# zzz
# OutputCopy
# NO
# YES
# NO
# YES
# YES
# NO
# YES
# NO
# Note
# In the first test case, s
#  will keep the same after any operations. However, the reversal of a
#  is still a
# , so it is impossible to make s
#  universal.

# In the second test case, the string rev
#  is lexicographically smaller than ver
# . Thus, s
#  is already universal.

# In the fifth test case, you can perform the operations as follows:

# Swap s4
#  and s7
# . After this operation, s
#  becomes uniserval
# ;
# Swap s1
#  and s3
# . After this operation, s
#  becomes inuserval
# .
# And the string inuserval
#  is universal.

import sys

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    if len(set(s)) == 1:
        output.append('NO')
        continue
    
    if k > 0:
        output.append('YES')
    else:
        reversed_s = ''.join(list(reversed(s)))
        if s < reversed_s:
            output.append('YES')
        else:
            output.append('NO')
            
print('\n'.join(output))