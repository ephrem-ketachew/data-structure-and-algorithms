# 1318. Minimum Flips to Make a OR b Equal to c
# Medium

# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

# Example 1:

# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
# Example 2:

# Input: a = 4, b = 2, c = 7
# Output: 1
# Example 3:

# Input: a = 1, b = 2, c = 3
# Output: 0

# Constraints:

# 1 <= a <= 10^9
# 1 <= b <= 10^9
# 1 <= c <= 10^9

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # max_bit_len = max(a.bit_length(), b.bit_length(), c.bit_length())
        # a_bin = bin(a)[2:].zfill(max_bit_len)
        # b_bin = bin(b)[2:].zfill(max_bit_len)
        # c_bin = bin(c)[2:].zfill(max_bit_len)
        
        # ops = 0
        # for i in range(max_bit_len):
        #     actual = int(a_bin[i]) | int(b_bin[i])
        #     expected = int(c_bin[i])
        #     if actual != expected:
        #         if expected == 1:
        #             ops += 1
        #         else:
        #             ops += int(a_bin[i]) + int(b_bin[i])
                    
        # return ops
        
        flips = 0
        for i in range(30):
            abit = (a >> i) & 1
            bbit = (b >> i) & 1
            cbit = (c >> i) & 1
            
            if cbit == 1:
                if abit | bbit == 0:
                    flips += 1
            else:
                flips += abit + bbit
                
                
        return flips