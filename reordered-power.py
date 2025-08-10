# 869. Reordered Power of 2
# Medium
# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

# Return true if and only if we can do this so that the resulting number is a power of two.

# Example 1:

# Input: n = 1
# Output: true
# Example 2:

# Input: n = 10
# Output: false

# Constraints:

# 1 <= n <= 109

from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power = ['1', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048', '4096', '8192', '16384', '32768', '65536', '131072', '262144', '524288', '1048576', '2097152', '4194304', '8388608', '16777216', '33554432', '67108864', '134217728', '268435456', '536870912', '1073741824']
        
        n = str(n)
        num_count = Counter(n)
        for num in power:
            if len(num) > len(n):
                return False
            if len(num) == len(n):
                if Counter(num) == num_count:
                    return True
        
        return False
        
# solution = Solution()
# print(solution.reorderedPowerOf2(n=635))