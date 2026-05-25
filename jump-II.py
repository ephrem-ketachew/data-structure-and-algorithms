# 1871. Jump Game VII
# Medium

# You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

# i + minJump <= j <= min(i + maxJump, s.length - 1), and
# s[j] == '0'.
# Return true if you can reach index s.length - 1 in s, or false otherwise.

# Example 1:

# Input: s = "011010", minJump = 2, maxJump = 3
# Output: true
# Explanation:
# In the first step, move from index 0 to index 3. 
# In the second step, move from index 3 to index 5.
# Example 2:

# Input: s = "01101110", minJump = 2, maxJump = 3
# Output: false

# Constraints:

# 2 <= s.length <= 105
# s[i] is either '0' or '1'.
# s[0] == '0'
# 1 <= minJump <= maxJump < s.length

from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        
        dq = deque([0])
        end = 0
        while dq:
            node = dq.popleft()
            start = max(node + minJump, end + 1)
            end = min(node + maxJump, len(s) - 1)
            for neighbor in range(start, end + 1):
                if s[neighbor] == '0':
                    if neighbor == len(s) - 1:
                        return True
                    dq.append(neighbor)
                    
        return False
                    