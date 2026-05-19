# 743. Network Delay Time
# Medium

# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

# Example 1:

# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# Example 2:

# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# Example 3:

# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
 
# Constraints:

# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        k -= 1
        for i in range(len(times)):
            u, v, w = times[i]
            times[i] = [u - 1, v - 1, w]
            
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
            
        dist = [float('inf')] * n
        dist[k] = 0
        
        min_heap = [(0, k)]
        while min_heap:
            current_time, node = heapq.heappop(min_heap)
            if current_time > dist[node]:
                continue
            
            for neighbor, time in adj[node]:
                new_time = current_time + time
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(min_heap, (new_time, neighbor))
                    
        time_taken = max(dist)      
        return time_taken if time_taken != float('inf') else -1