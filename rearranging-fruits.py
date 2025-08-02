# 2561. Rearranging Fruits
# Hard
# You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:

# Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
# The cost of the swap is min(basket1[i],basket2[j]).
# Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

# Return the minimum cost to make both the baskets equal or -1 if impossible.

# Example 1:

# Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
# Output: 1
# Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.
# Example 2:

# Input: basket1 = [2,3,4,1], basket2 = [3,2,5,1]
# Output: -1
# Explanation: It can be shown that it is impossible to make both the baskets equal.
 
# Constraints:
# basket1.length == basket2.length
# 1 <= basket1.length <= 105
# 1 <= basket1[i],basket2[i] <= 109

from typing import List
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        counter1 = Counter(basket1)
        counter2 = Counter(basket2)
        
        for num in counter1:
            if (counter1[num] + counter2[num]) % 2:
                return -1
            
        basket_swap = []        
        for num in counter1:
            diff = counter1[num] - counter2[num]
            if diff > 0:
                basket_swap.extend([num] * (diff // 2))
        for num in counter2:
            diff = counter2[num] - counter1[num]
            if diff > 0:
                basket_swap.extend([num] * (diff // 2))

        minn = min(min(basket1), min(basket2))
        basket_swap.sort()

        i = min_swaps = 0
        for count in range(len(basket_swap) // 2):
            if basket_swap[i] < minn * 2:
                min_swaps += basket_swap[i]
                i += 1
            else:
                min_swaps += minn * 2
            count += 1

        return min_swaps
        
# solution = Solution()
# basket1 = [4,2,2,2]
# basket2 = [1,4,1,2]
# basket1 = [84,80,43,8,80,88,43,14,100,88]
# basket2 = [32,32,42,68,68,100,42,84,14,8]
# print(solution.minCost(basket1, basket2))