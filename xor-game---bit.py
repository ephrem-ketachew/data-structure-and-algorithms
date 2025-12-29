# 810. Chalkboard XOR Game
# Hard

# You are given an array of integers nums represents the numbers written on a chalkboard.

# Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first. If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become 0, then that player loses. The bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.

# Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.

# Return true if and only if Alice wins the game, assuming both players play optimally.

# Example 1:

# Input: nums = [1,1,2]
# Output: false
# Explanation: 
# Alice has two choices: erase 1 or erase 2. 
# If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he wants, because Alice will be the one to erase the last element and she will lose. 
# If Alice erases 2 first, now nums become [1, 1]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.
# Example 2:

# Input: nums = [0,1]
# Output: true
# Example 3:

# Input: nums = [1,2,3]
# Output: true

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] < 216

from typing import List 
from collections import Counter
from functools import reduce
from operator import xor

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        # counter = Counter(nums)
        # odds = []
        # for num in counter:
        #     if counter[num] % 2:
        #         odds.append(num)
                
        # if len(odds) == 0:
        #     return True
            
        # cur_xor = reduce(xor, odds)    
        # turn = 0
        # while len(odds) > 1:
        #     if cur_xor == 0:
        #         if turn == 0:
        #             return True
        #         return False
            
        #     removed_num = odds.pop()
        #     if removed_num == cur_xor:
        #         temp = odds.pop()
        #         odds.append(removed_num)
        #         removed_num = temp
                
        #     cur_xor ^= removed_num
                
        #     turn ^= 1

        # if turn == 0:
        #     return odds[0] == 0
        
        # return odds[0] != 0
        
        return reduce(xor, nums) == 0 or len(nums) % 2 == 0