# 1061. Lexicographically Smallest Equivalent String
# Medium

# You are given two strings of the same length s1 and s2 and a string baseStr.

# We say s1[i] and s2[i] are equivalent characters.

# For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
# Equivalent characters follow the usual rules of any equivalence relation:

# Reflexivity: 'a' == 'a'.
# Symmetry: 'a' == 'b' implies 'b' == 'a'.
# Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
# For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

# Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.

# Example 1:

# Input: s1 = "parker", s2 = "morris", baseStr = "parser"
# Output: "makkek"
# Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
# The characters in each group are equivalent and sorted in lexicographical order.
# So the answer is "makkek".
# Example 2:

# Input: s1 = "hello", s2 = "world", baseStr = "hold"
# Output: "hdld"
# Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
# So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".
# Example 3:

# Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
# Output: "aauaaaaada"
# Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".

# Constraints:

# 1 <= s1.length, s2.length, baseStr <= 1000
# s1.length == s2.length
# s1, s2, and baseStr consist of lowercase English letters.

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
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dsu = DSU()
        for i in range(len(s1)):
            num1, num2 = ord(s1[i]) - 97, ord(s2[i]) - 97
            dsu.union(num1, num2)
            
        mins = list(range(26))
        keys = list(range(26))
        for i in range(26):
            key = dsu.find(i)
            mins[key] = min(mins[key], i)
            keys[i] = key
            
        ans = []
        for ch in baseStr:
            num = ord(ch) - 97
            key = keys[num]
            ans.append(chr(mins[key]+ 97))
            
        return ''.join(ans)