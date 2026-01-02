# 3211. Generate Binary Strings Without Adjacent Zeros
# Medium

# You are given a positive integer n.

# A binary string x is valid if all substrings of x of length 2 contain at least one "1".

# Return all valid strings with length n, in any order.

# Example 1:

# Input: n = 3

# Output: ["010","011","101","110","111"]

# Explanation:

# The valid strings of length 3 are: "010", "011", "101", "110", and "111".

# Example 2:

# Input: n = 1

# Output: ["0","1"]

# Explanation:

# The valid strings of length 1 are: "0" and "1".

# Constraints:

# 1 <= n <= 18

from typing import List

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        for i in range(2 ** n):
            subset = ['0'] * n
            for bit in range(n):
                if i & (1 << bit):
                    subset[bit] = '1'
            for k in range(1, n):
                if not (int(subset[k - 1]) | int(subset[k])):
                    break
            else:
                ans.append(''.join(subset))
                
        return ans