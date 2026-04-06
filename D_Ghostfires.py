# D. Ghostfires
# time limit per test2 seconds
# memory limit per test256 megabytes

# OtterZ decided to make a weapon using ghostfires. He collected several ghostfires in colors red, green, and blue. He will put some of the ghostfires in a row to build the weapon. To make the weapon more powerful, OtterZ will use as many ghostfires as possible, but the weapon will be out of control if there are two ghostfires of the same color adjacent or separated by exactly two ghostfires in the row.

# Formally, OtterZ collected r
#  red ghostfires, g
#  green ghostfires, and b
#  blue ghostfires. He wants to construct a string s
#  consisting of the characters 'R', 'G', and 'B' that satisfies the following conditions:

# The number of occurrences of 'R', 'G', and 'B' in s
#  does not exceed r
# , g
# , and b
# , respectively.
# For all 1≤i≤|s|−1
# , si≠si+1
# .
# For all 1≤i≤|s|−3
# , si≠si+3
# .
# The length of s
#  is the maximum possible.
# Help OtterZ to construct the row. Although there may be several possible rows, OtterZ just requires one of them.

# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.

# The only line of each test case contains three integers r
# , g
# , and b
#  (0≤r,g,b≤106
# , r+g+b>0
# ), representing the number of red, green, and blue ghostfires, respectively.

# It is guaranteed that the sum of r+g+b
#  over all test cases does not exceed 106
# .

# Output
# For each query, output a string s
#  consisting of the characters 'R', 'G', and 'B', where si
#  equals 'R', 'G' or 'B' indicates that the i
# -th ghostfire is colored red, green, or blue, respectively.

# If there are multiple answers, output any.

# Example
# InputCopy
# 5
# 0 0 1
# 1 1 1
# 0 3 0
# 2 2 2
# 2 7 3
# OutputCopy
# B
# RGB
# G
# GBRBRG
# GRGRGBGBGBG
# Note
# For the first test case, "B" is the only valid construction.

# For the second test case, "RGB", "RBG", "GRB", "GRB", "BRG", and "BGR" are all correct.

# For the third test case, "GG" and "GGG" are invalid because s1=s2
# .

import sys

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    r, g, b = map(int, input().split())
    
    count = {'R': r, 'G': g, 'B': b}
    
    ans = []
    while True:
        best_color = None
        best_match = -1
        best_freq = -1
        for color in ['R', 'G', 'B']:
            if count[color] == 0:
                continue

            if ans and color == ans[-1]:
                continue
            
            if len(ans) >= 3 and ans[-3] == color:
                continue
            
            match = 1 if len(ans) >= 2 and ans[-2] == color else 0
            
            if count[color] > best_freq or (count[color] == best_freq and match > best_match):
                best_match = match
                best_color = color
                best_freq = count[color]
            
        if best_color is None:
            break
        
        ans.append(best_color)
        count[best_color] -= 1
            
    output.append(''.join(ans))
    
print('\n'.join(output))