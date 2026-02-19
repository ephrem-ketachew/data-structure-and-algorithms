# 1545. Find Kth Bit in Nth Binary String
# Medium

# Given two positive integers n and k, the binary string Sn is formed as follows:

# S1 = "0"
# Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
# Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

# For example, the first four strings in the above sequence are:

# S1 = "0"
# S2 = "011"
# S3 = "0111001"
# S4 = "011100110110001"
# Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

# Example 1:

# Input: n = 3, k = 1
# Output: "0"
# Explanation: S3 is "0111001".
# The 1st bit is "0".
# Example 2:

# Input: n = 4, k = 11
# Output: "1"
# Explanation: S4 is "011100110110001".
# The 11th bit is "1".

# Constraints:

# 1 <= n <= 20
# 1 <= k <= 2n - 1

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # s = [0]
        # while len(s) < k:
        #     s_inv = [0] * len(s)
        #     for i in range(len(s)):
        #         s_inv[i] = s[i] ^ 1
        #     s_inv.reverse()
        #     s = s + [1] + s_inv
        # return str(s[k - 1])
        
        # def __find_kth_bit(n):
        #     if n == 1:
        #         return [0]
            
        #     n_1 = __find_kth_bit(n - 1)
        #     n_1_inv = [0] * len(n_1)
        #     for i in range(len(n_1_inv)):
        #         n_1_inv[i] = n_1[i] ^ 1
        #     n_1_inv.reverse()
            
        #     return n_1 + [1] + n_1_inv
        
        # return str(__find_kth_bit(n)[k - 1])
        
        if n == 1:
            return '0'
        
        length = (1 << n ) - 1
        mid = length // 2 + 1
        
        if k == mid:
            return '1'
        
        if k < mid:
            return self.findKthBit(n - 1, k)
        
        mirror_k = length - k + 1
        mirrored_bit = self.findKthBit(n - 1, mirror_k)
        
        return '0' if mirrored_bit == '1' else '1'