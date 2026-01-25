# 201. Bitwise AND of Numbers Range
# Medium

# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

# Example 1:

# Input: left = 5, right = 7
# Output: 4
# Example 2:

# Input: left = 0, right = 0
# Output: 0
# Example 3:

# Input: left = 1, right = 2147483647
# Output: 0
 

# Constraints:

# 0 <= left <= right <= 231 - 1

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # WRONG APPROACH😭
        # bit_len = right.bit_length()
        # mask = 0
        # for i in range(bit_len):
        #     num_ibit_unset = right & ~(1 << i)
        #     if num_ibit_unset < left and right > num_ibit_unset:
        #         mask |= 1 << i
                
        # return mask
        
        
        # STANDARD APPROACH
        # shift = 0
        # while left < right:
        #     left >>= 1
        #     right >>= 1
        #     shift += 1
            
        # return left << shift

        # RESURRECTION FOR MY INTUITIVE APPROACH
        mask = 0
        bit_len = right.bit_length()
        for i in range(bit_len):
            bit_val = 1 << i
            if left & bit_val and right & bit_val:
                num_ibit_unset = right - bit_val
                if num_ibit_unset < left:
                    mask |= bit_val
                    
        return mask