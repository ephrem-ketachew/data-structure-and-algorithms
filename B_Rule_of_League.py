# B. Rule of League
# time limit per test2 seconds
# memory limit per test256 megabytes
# There is a badminton championship in which n
#  players take part. The players are numbered from 1
#  to n
# .

# The championship proceeds as follows: player 1
#  and player 2
#  play a game, then the winner and player 3
#  play a game, and then the winner and player 4
#  play a game, and so on. So, n−1
#  games are played, and the winner of the last game becomes the champion. There are no draws in the games.

# You want to find out the result of championship. Currently, you only know the following information:

# Each player has either won x
#  games or y
#  games in the championship.
# Given n
# , x
# , and y
# , find out if there is a result that matches this information.

# Input
# The first line contains one integer t
#  (1≤t≤105
# ) — the number of test cases.

# The only line of each test case contains three integers n
# , x
# , y
#  (2≤n≤105
# , 0≤x,y<n
# ).

# It is guaranteed that the sum of n
#  over all test cases doesn't exceed 2⋅105
# .

# Output
# Print the answer for each test case, one per line. If there is no result that matches the given information about n
# , x
# , y
# , print −1
# . Otherwise, print n−1
#  space separated integers, where the i
# -th integer is the player number of the winner of the i
# -th game.

# If there are multiple valid results, print any.

# Example
# InputCopy
# 5
# 5 2 0
# 8 1 2
# 3 0 0
# 2 0 1
# 6 3 0
# OutputCopy
# 1 1 4 4
# -1
# -1
# 2 
# -1
# Note
# In the first test case, player 1
#  and player 4
#  won x
#  times, player 2
#  and player 3
#  won y
#  times.

# In the second, third, and fifth test cases, no valid result exists.

import sys

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n, x, y = map(int, input().split())
    if (x != 0 and y != 0) or (x == 0 and y == 0):
        output.append('-1')
        continue
        
    w = max(x, y)
        
    if (n - 1) % w != 0:
        output.append('-1')
        continue
    
    ans = []
    current_winner = 1
    num_streaks = (n - 1) // w
    
    for step in range(num_streaks):
        ans.extend([str(current_winner)] * w)
        
        if current_winner == 1:
            current_winner = w + 2
        else:
            current_winner += w
            
    output.append(' '.join(ans))
        
print('\n'.join(output))