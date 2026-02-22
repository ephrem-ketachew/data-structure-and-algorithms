# 3782. Last Remaining Integer After Alternating Deletion Operations
# Hard

# You are given an integer n.

# We write the integers from 1 to n in a sequence from left to right. Then, alternately apply the following two operations until only one integer remains, starting with operation 1:

# Operation 1: Starting from the left, delete every second number.
# Operation 2: Starting from the right, delete every second number.
# Return the last remaining integer.

# Example 1:

# Input: n = 8

# Output: 3

# Explanation:

# Write [1, 2, 3, 4, 5, 6, 7, 8] in a sequence.
# Starting from the left, we delete every second number: [1, 2, 3, 4, 5, 6, 7, 8]. The remaining integers are [1, 3, 5, 7].
# Starting from the right, we delete every second number: [1, 3, 5, 7]. The remaining integers are [3, 7].
# Starting from the left, we delete every second number: [3, 7]. The remaining integer is [3].
# Example 2:

# Input: n = 5

# Output: 1

# Explanation:

# Write [1, 2, 3, 4, 5] in a sequence.
# Starting from the left, we delete every second number: [1, 2, 3, 4, 5]. The remaining integers are [1, 3, 5].
# Starting from the right, we delete every second number: [1, 3, 5]. The remaining integers are [1, 5].
# Starting from the left, we delete every second number: [1, 5]. The remaining integer is [1].
# Example 3:

# Input: n = 1

# Output: 1

# Explanation:

# Write [1] in a sequence.
# The last remaining integer is 1.
 

# Constraints:

# 1 <= n <= 1015

from typing import List

class Solution:
    def lastInteger(self, n: int) -> int:
        # def _last_integer(arr: List[int], turn):
        #     if len(arr) == 1:
        #         return arr[0]
            
        #     if turn == 0:
        #         return _last_integer([num for i, num in enumerate(arr) if i % 2 == 0], 1)
        #     else:
        #         if len(arr) % 2 == 1:
        #             return _last_integer([num for i, num in enumerate(arr) if i % 2 == 0], 0)
        #         else:
        #             return _last_integer([num for i, num in enumerate(arr) if i % 2 == 1], 0)
                
        # return _last_integer(list(range(1, n + 1)), 0)
    
        def _last_integer(start: int, turn: int, length: int, inc: int):
            if length == 1:
                return start
            
            if turn == 0:
                return _last_integer(start, 1, (length + 1) // 2, inc * 2)
            else:
                if length % 2 == 1:
                    return _last_integer(start, 0, (length + 1) // 2, inc * 2)
                else:
                    return _last_integer(start + inc, 0, length // 2, inc * 2)
                
        return _last_integer(1, 0, n, 1)
            