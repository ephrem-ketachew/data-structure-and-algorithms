# 990. Satisfiability of Equality Equations
# Medium

# You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

# Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

# Example 1:

# Input: equations = ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
# There is no way to assign the variables to satisfy both equations.
# Example 2:

# Input: equations = ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
 
# Constraints:

# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] is a lowercase letter.
# equations[i][1] is either '=' or '!'.
# equations[i][2] is '='.
# equations[i][3] is a lowercase letter.

from typing import List

class DSU:
    def __init__(self) -> None:
        self.parent = list(range(26))
        self.rank = [1] * 26
        
    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = DSU()
        not_equal = []
        for equation in equations:
            a, op, _, b = equation
            a, b = ord(a) - 97, ord(b) - 97
            if op == '=':
                dsu.union(a, b)
            else:
                not_equal.append((a, b))
             
        for a, b in not_equal:
            if dsu.find(a) == dsu.find(b):
                return False
            
        return True