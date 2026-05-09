# 210. Course Schedule II
# Medium

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]
 
# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.

from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        for u, v in prerequisites:
            in_degree[u] += 1
            adj[v].append(u)
            
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
                
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        
        return result if len(result) == numCourses else []
    
        # adj = defaultdict(list)
        # for a, b in prerequisites:
        #     adj[a].append(b)
            
        # def dfs(node: int) -> List[int]:
        #     if state[node] == 1:
        #         return [-1]
            
        #     if state[node] == 2:
        #         return []
            
        #     state[node] = 1
        #     order = []
        #     for neighbor in adj[node]:
        #         arr = dfs(neighbor)
        #         if len(arr) == 1 and arr[0] == -1:
        #             return [-1]
                
        #         order.extend(arr)
                
        #     order.append(node)
        #     state[node] = 2
        #     return order
        
        
        # state = [0] * numCourses
        # order = []
        # for i in range(numCourses):
        #     if state[i] == 0:
        #         curr = dfs(i)
        #         if len(curr) == 1 and curr[0] == -1:
        #             return []
        #         order.extend(curr)
                
        # return order
        
        # adj = defaultdict(list)
        # for a, b in prerequisites:
        #     adj[a].append(b)
            
        # state = [0] * numCourses
        # order = []
        # def dfs(node: int) -> bool:
        #     if state[node] == 2:
        #         return False
            
        #     if state[node] == 1:
        #         return True
            
        #     state[node] = 1
        #     for neighbor in adj[node]:
        #         if dfs(neighbor):
        #             return True
                
        #     order.append(node)
        #     state[node] = 2
            
        #     return False
        
        # for i in range(numCourses):
        #     if state[i] == 0:
        #         if dfs(i):
        #             return []
                
        # return order