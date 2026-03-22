# A. Not a Substring
# time limit per test2 seconds
# memory limit per test256 megabytes
# A bracket sequence is a string consisting of characters '(' and/or ')'. A regular bracket sequence is a bracket sequence that can be transformed into a correct arithmetic expression by inserting characters '1' and '+' between the original characters of the sequence. For example:

# bracket sequences "()()" and "(())" are regular (they can be transformed into "(1)+(1)" and "((1+1)+1)", respectively);
# bracket sequences ")(", "(" and ")" are not regular.
# You are given a bracket sequence s
# ; let's define its length as n
# . Your task is to find a regular bracket sequence t
#  of length 2n
#  such that s
#  does not occur in t
#  as a contiguous substring, or report that there is no such sequence.

# Input
# The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.

# The only line of each test case contains a string s
#  (2≤|s|≤50
# ), consisting of characters "(" and/or ")".

# Output
# For each test case, print the answer to it. If there is no required regular bracket sequence, print NO in a separate line. Otherwise, print YES in the first line, and the required regular bracket sequence t
#  itself in the second line. If there are multiple answers — you may print any of them.

# Example
# InputCopy
# 4
# )(
# (()
# ()
# ))()
# OutputCopy
# YES
# (())
# YES
# ()()()
# NO
# YES
# ()(()())

import sys

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    s = input().strip()
    if s == '()':
        output.append('NO')
        continue
    
    output.append('YES')
    n = len(s) 
    valid_seq = '()' * n
    if s not in valid_seq:
        output.append(valid_seq)
    else:
        output.append('(' * n + ')' * n)
        
print('\n'.join(output))