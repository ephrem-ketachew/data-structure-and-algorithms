# 556. Next Greater Element III
# Medium
# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

# Example 1:

# Input: n = 12
# Output: 21
# Example 2:

# Input: n = 21
# Output: -1

# Constraints:

# 1 <= n <= 231 - 1

from bisect import bisect_right

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        MAX_LIMIT = 2 ** 31 - 1
        
        s = list(str(n))
        i = len(s) - 2
        
        while i >= 0 and s[i] >= s[i + 1]:
            i -= 1
            
        if i == -1:
            return -1
        
        left_arr = s[:i:-1]
        index = bisect_right(left_arr, s[i])
        s[i], left_arr[index] = left_arr[index], s[i]
        s[i + 1:] = left_arr
        
        num = int(''.join(s))
        if num > MAX_LIMIT:
            return - 1
        
        return num
    
# solution = Solution()
# n = 12
# n = 2147483486
# print(solution.nextGreaterElement(n))