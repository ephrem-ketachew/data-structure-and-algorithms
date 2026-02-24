# 390. Elimination Game
# Medium

# You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following algorithm on arr:

# Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
# Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
# Keep repeating the steps again, alternating left to right and right to left, until a single number remains.
# Given the integer n, return the last number that remains in arr.

# Example 1:

# Input: n = 9
# Output: 6
# Explanation:
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = [2, 4, 6, 8]
# arr = [2, 6]
# arr = [6]
# Example 2:

# Input: n = 1
# Output: 1

# Constraints:

# 1 <= n <= 109

from typing import List

class Solution:
    def lastRemaining(self, n: int) -> int:
        # def _last_remaining(arr: List[int], idx) -> int:
        #     if len(arr) == 1:
        #         return arr[0]
            
        #     if idx == 0:
        #         arr = [num for i, num in enumerate(arr) if i % 2 == 1]
        #     else:
        #         if len(arr) % 2 == 1:
        #             arr = [num for i, num in enumerate(arr) if i % 2 == 0]
        #         else:
        #             arr = [num for i, num in enumerate(arr) if i % 2 == 1]
                
        #     idx ^= 1
            
        #     return _last_remaining(arr, idx)
        
        # return _last_remaining(range(1, n + 1), 0)
        
        left = 0
        remain = n
        step = 1
        head = 1
        while remain > 1:
            if left == 0 or remain % 2 == 1:
                head += step
                
            step *= 2
            
            remain //= 2
            
            left ^= 1
            
        return head
            