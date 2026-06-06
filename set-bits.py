# Q1. Exactly One Consecutive Set Bits Pair
# Easy

# You are given an integer n.

# Return true if its binary representation contains exactly one pair of consecutive set bits, and false otherwise.

# The set bits in an integer are the 1's present when it is written in binary.

# Example 1:

# Input: nums = 6

# Output: true

# Explanation:

# Binary representation of 6 is 110.
# There is exactly one pair of consecutive set bits ("11"). Thus, the answer is true​​​​​​​.
# Example 2:

# Input: nums = 5

# Output: false

# Explanation:

# Binary representation of 5 is 101.
# There are no consecutive set bits. Thus, the answer is false​​​​​​​.

# Constraints:

# 0 <= n <= 105©leetcode

class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        num = bin(n)[2:]
        count = 0
        for i in range(1, len(num)):
            if num[i] == num[i - 1] == '1':
                count += 1
                
        return count == 1