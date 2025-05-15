# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
MAX_LIMIT = 2 ** 31 - 1
MIN_LIMIT = -2 ** 31
class Solution:
    def reverse(self, x: int) -> int:
        reversed_x = int(''.join(list(reversed(str(abs(x))))))
        reversed_x = reversed_x * -1 if x < 0 else reversed_x
        return 0 if reversed_x < MIN_LIMIT or reversed_x > MAX_LIMIT else reversed_x
    