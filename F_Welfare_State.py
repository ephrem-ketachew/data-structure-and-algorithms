import sys 
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
q = int(input())

b = [[num, 0] for num in a]
events = []
for i in range(q):
    arr = input().split()
    
    if len(arr) == 3:
        p = int(arr[1]) - 1
        x = int(arr[2])
        
        b[p] = [x, i + 1]
        
    else:
        x = int(arr[1])
        events.append([x, i + 1])
        
max_suffix = []
max_num = 0
for i in range(len(events) - 1, -1, -1):
    max_num = max(max_num, events[i][0])
    max_suffix.append([max_num, events[i][1]])
    
max_suffix.reverse()

ans = []
for i in range(n):
    num, t0 = b[i]
    last_max_idx = bisect_left(max_suffix, t0, key=lambda x: x[1])
    if last_max_idx < len(max_suffix):
        num = max(num, max_suffix[last_max_idx][0])
    
    ans.append(num)
    
print(*ans)