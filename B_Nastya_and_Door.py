# B. Nastya and Door
# time limit per test1 second
# memory limit per test256 megabytes
# On February 14 Denis decided to give Valentine to Nastya and did not come up with anything better than to draw a huge red heart on the door of the length k
#  (k≥3
# ). Nastya was very confused by this present, so she decided to break the door, throwing it on the mountains.

# Mountains are described by a sequence of heights a1,a2,…,an
#  in order from left to right (k≤n
# ). It is guaranteed that neighboring heights are not equal to each other (that is, ai≠ai+1
#  for all i
#  from 1
#  to n−1
# ).

# Peaks of mountains on the segment [l,r]
#  (from l
#  to r
# ) are called indexes i
#  such that l<i<r
# , ai−1<ai
#  and ai>ai+1
# . It is worth noting that the boundary indexes l
#  and r
#  for the segment are not peaks. For example, if n=8
#  and a=[3,1,4,1,5,9,2,6]
# , then the segment [1,8]
#  has only two peaks (with indexes 3
#  and 6
# ), and there are no peaks on the segment [3,6]
# .

# To break the door, Nastya throws it to a segment [l,l+k−1]
#  of consecutive mountains of length k
#  (1≤l≤n−k+1
# ). When the door touches the peaks of the mountains, it breaks into two parts, after that these parts will continue to fall in different halves and also break into pieces when touching the peaks of the mountains, and so on. Formally, the number of parts that the door will break into will be equal to p+1
# , where p
#  is the number of peaks on the segment [l,l+k−1]
# .

# Nastya wants to break it into as many pieces as possible. Help her choose such a segment of mountains [l,l+k−1]
#  that the number of peaks on it is maximum. If there are several optimal segments, Nastya wants to find one for which the value l
#  is minimal.

# Formally, you need to choose a segment of mountains [l,l+k−1]
#  that has the maximum number of peaks. Among all such segments, you need to find the segment that has the minimum possible value l
# .

# Input
# The first line contains an integer t
#  (1≤t≤104
# )  — the number of test cases. Then the descriptions of the test cases follow.

# The first line of each test case contains two integers n
#  and k
#  (3≤k≤n≤2⋅105
# )  — the number of mountains and the length of the door.

# The second line of the input data set contains n
#  integers a1,a2,…,an
#  (0≤ai≤109
# , ai≠ai+1
# )  — the heights of mountains.

# It is guaranteed that the sum of n
#  over all the test cases will not exceed 2⋅105
# .

# Output
# For each test case, output two integers t
#  and l
#   — the maximum number of parts that the door can split into, and the left border of the segment of length k
#  that the door should be reset to.

# Example
# InputCopy
# 5
# 8 6
# 1 2 4 1 2 4 1 2
# 5 3
# 3 2 3 2 1
# 10 4
# 4 3 4 3 2 3 2 1 0 1
# 15 7
# 3 7 4 8 2 3 4 5 21 2 3 4 2 1 3
# 7 5
# 1 2 3 4 5 6 1
# OutputCopy
# 3 2
# 2 2
# 2 1
# 3 1
# 2 3
# Note
# In the first example, you need to select a segment of mountains from 2
#  to 7
# . In this segment, the indexes 3
#  and 6
#  are peaks, so the answer is 3
#  (only 2
#  peaks, so the door will break into 3
#  parts). It is not difficult to notice that the mountain segments [1,6]
#  and [3,8]
#  are not suitable since they only have a 1
#  peak (for the first segment, the 6
#  index is not a peak, and for the second segment, the 3
#  index is not a peak).

# In the second example, you need to select a segment of mountains from 2
#  to 4
# . In this segment, the index 3
#  is a peak, so the answer is 2
#  (only 1
#  peak, so the door will break into 2
#  parts).

# In the third example, you need to select a segment of mountains from 1
#  to 4
# . In this segment, the index 3
#  is a peak, so the answer is 2
#  (only 1
#  peak, so the door will break into 2
#  parts). You can see that on the segments [2,5]
# , [4,7]
#  and [5,8]
#  the number of peaks is also 1
# , but these segments have a left border greater than the segment [1,4]
# , so they are not the correct answer.

import sys

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    win_peaks = 0
    left = 0
    for right in range(1, k - 1):
        if a[right - 1] < a[right] and a[right] > a[right + 1]:
            win_peaks += 1
            
    max_peaks = win_peaks
    start = 0
    for right in range(k - 1, n - 1):
        left_idx = right - (k - 2)
        if a[left_idx - 1] < a[left_idx] and a[left_idx] > a[left_idx + 1]:
            win_peaks -= 1
            
        if a[right - 1] < a[right] and a[right] > a[right + 1]:
            win_peaks += 1
            
        if win_peaks > max_peaks:
            max_peaks = win_peaks
            start = left_idx
            
    output.append(f'{max_peaks + 1} {start + 1}')
    
print('\n'.join(output))