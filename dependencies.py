# 1203. Sort Items by Groups Respecting Dependencies
# Hard

# There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

# Return a sorted list of the items such that:

# The items that belong to the same group are next to each other in the sorted list.
# There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
# Return any solution if there is more than one solution and return an empty list if there is no solution.

# Example 1:

# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
# Output: [6,3,4,1,5,2,0,7]
# Example 2:

# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
# Output: []
# Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.

# Constraints:

# 1 <= m <= n <= 3 * 104
# group.length == beforeItems.length == n
# -1 <= group[i] <= m - 1
# 0 <= beforeItems[i].length <= n - 1
# 0 <= beforeItems[i][j] <= n - 1
# i != beforeItems[i][j]
# beforeItems[i] does not contain duplicates elements.

from typing import List
from collections import defaultdict, deque

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
                
        groups_adj = defaultdict(list)
        items_adj = defaultdict(list)
        groups_in_degree = [0] * m
        items_in_degree = [0] * n
        for i, items in enumerate(beforeItems):
            curr_group = group[i]
            for prev_item in items:
                prev_group = group[prev_item]
                
                items_in_degree[i] += 1
                items_adj[prev_item].append(i)
                
                if prev_group != curr_group:
                    groups_in_degree[curr_group] += 1
                    groups_adj[prev_group].append(curr_group)
                    
        def topo_sort(adj: defaultdict[list], in_degree: List[int], length: int) -> List[int]:
            queue = deque([i for i in range(length) if in_degree[i] == 0])
            result = []
            while queue:
                node = queue.popleft()
                result.append(node)
                for neighbor in adj[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
                        
            return result if len(result) == length else []
        
        groups_order = topo_sort(groups_adj, groups_in_degree, m)
        items_order = topo_sort(items_adj, items_in_degree, n)
        
        if not groups_order or not items_order:
            return []
        
        items_bucket = defaultdict(list)
        for item in items_order:
            group_id = group[item]
            items_bucket[group_id].append(item)
            
        ans = []
        for group_id in groups_order:
            ans.extend(items_bucket[group_id])
            
        return ans