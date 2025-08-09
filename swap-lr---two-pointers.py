# 777. Swap Adjacent in LR String
# Medium
# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string result, return True if and only if there exists a sequence of moves to transform start to result.

# Example 1:

# Input: start = "RXXLRXRXL", result = "XRLXXRRLX"
# Output: true
# Explanation: We can transform start to result following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# Example 2:

# Input: start = "X", result = "L"
# Output: false

# Constraints:

# 1 <= start.length <= 104
# start.length == result.length
# Both start and result will only consist of characters in 'L', 'R', and 'X'.

class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if start.replace('X', '') != result.replace('X', ''):
            return False
        
        n = len(start)
        i = j = 0
        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and result[j] == 'X':
                j += 1
                
            if i == j == n:
                return True
                
            if start[i] == 'L':
                if j > i:
                    return False
            
            elif start[i] == 'R':
                if j < i:
                    return False
                
            i += 1
            j += 1
                
        return True
    
# solution = Solution()
# start = "RXXLRXRXL"
# result = "XRLXXRRLX"
# start = "XXXXXLXXXX"
# result = "LXXXXXXXXX"
# print(solution.canTransform(start, result))