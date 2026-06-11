# 952. Largest Component Size by Common Factor
# Hard

# You are given an integer array of unique positive integers nums. Consider the following graph:

# There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
# There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
# Return the size of the largest connected component in the graph.

# Example 1:

# Input: nums = [4,6,15,35]
# Output: 4
# Example 2:

# Input: nums = [20,50,9,63]
# Output: 2
# Example 3:

# Input: nums = [2,3,6,7,4,12,21,39]
# Output: 8
 
# Constraints:

# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] <= 105
# All the values of nums are unique.

from typing import List
from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True
        

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        dsu = DSU(max(nums))
        for num in nums:
            i = 2
            n = num
            while i * i <= n:
                if n % i == 0:
                    dsu.union(num, i)
                    while n % i == 0:
                        n //= i
                i += 1
            if n > 1:
                dsu.union(num, n)

        components = defaultdict(int)
        for num in nums:
            key = dsu.find(num)
            components[key] += 1

        return max(components.values())