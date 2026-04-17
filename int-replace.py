# 397. Integer Replacement
# Medium

# Given a positive integer n, you can apply one of the following operations:

# If n is even, replace n with n / 2.
# If n is odd, replace n with either n + 1 or n - 1.
# Return the minimum number of operations needed for n to become 1.

# Example 1:

# Input: n = 8
# Output: 3
# Explanation: 8 -> 4 -> 2 -> 1
# Example 2:

# Input: n = 7
# Output: 4
# Explanation: 7 -> 8 -> 4 -> 2 -> 1
# or 7 -> 6 -> 3 -> 2 -> 1
# Example 3:

# Input: n = 4
# Output: 2

# Constraints:

# 1 <= n <= 231 - 1

from collections import deque

class Solution:
    def integerReplacement(self, n: int) -> int:
        queue = deque([n])
        seen = set([n])
        count = 0
        while queue:
            t = len(queue)
            for _ in range(t):
                num = queue.popleft()
                if num == 1:
                    return count
                
                if num % 2 == 0:
                    res = num // 2
                    if not res in seen:
                        queue.append(res)
                        seen.add(res)
                else:
                    for res in (num - 1, num + 1):
                        if not res in seen:
                            queue.append(res)
                            seen.add(res)
                            
            count += 1
            
        return count