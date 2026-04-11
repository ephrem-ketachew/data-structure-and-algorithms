# 1202. Smallest String With Swaps
# Medium

# You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

# You can swap the characters at any pair of indices in the given pairs any number of times.

# Return the lexicographically smallest string that s can be changed to after using the swaps.

# Example 1:

# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
# Example 2:

# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"
# Example 3:

# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination: 
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"

# Constraints:

# 1 <= s.length <= 10^5
# 0 <= pairs.length <= 10^5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s only contains lower case English letters.

from typing import List
from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(x: int, cycle: list) -> None:
            cycle.append(x)
            seen.add(x)
            for y in network[x]:
                if not y in seen:
                    dfs(y, cycle)
                
        network = defaultdict(list)
        for x, y in pairs:
            network[x].append(y)
            network[y].append(x)
           
        connected_components = []
        seen = set()
        for x in network:
            if x not in seen:
                cycle = []
                dfs(x, cycle)
                connected_components.append(cycle)
                
        arr = list(s)
        for cycle in connected_components:
            indices = sorted(cycle)
            chars = sorted(s[i] for i in indices)
            for i in range(len(indices)):
                idx = indices[i]
                arr[idx] = chars[i]
                
        return ''.join(arr)