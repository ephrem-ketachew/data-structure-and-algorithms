# 60. Permutation Sequence
# Hard

# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Example 1:

# Input: n = 3, k = 3
# Output: "213"
# Example 2:

# Input: n = 4, k = 9
# Output: "2314"
# Example 3:

# Input: n = 3, k = 1
# Output: "123"
 

# Constraints:

# 1 <= n <= 9
# 1 <= k <= n!

import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # res = []
        # def _get_permutation(seen: List[int]) -> None:
        #     if len(seen) == n:
        #         res.append(''.join(seen))
        #     for i in range(1, n + 1):
        #         if str(i) not in seen:
        #             _get_permutation(seen + [str(i)])
                    
        # _get_permutation([])
        # res.sort()
        
        # return res[k - 1]
                
        nums = [str(i) for i in range(1, n + 1)]
        res = ''
        k -= 1
        for i in range(n, 0, -1):
            block_size = math.factorial(i - 1)
            
            index = k // block_size
            
            res += nums.pop(index)
            
            k = k % block_size
            
        return res