# 2517. Maximum Tastiness of Candy Basket
# Medium

# You are given an array of positive integers price where price[i] denotes the price of the ith candy and a positive integer k.

# The store sells baskets of k distinct candies. The tastiness of a candy basket is the smallest absolute difference of the prices of any two candies in the basket.

# Return the maximum tastiness of a candy basket.

# Example 1:

# Input: price = [13,5,1,8,21,2], k = 3
# Output: 8
# Explanation: Choose the candies with the prices [13,5,21].
# The tastiness of the candy basket is: min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8.
# It can be proven that 8 is the maximum tastiness that can be achieved.
# Example 2:

# Input: price = [1,3,1], k = 2
# Output: 2
# Explanation: Choose the candies with the prices [1,3].
# The tastiness of the candy basket is: min(|1 - 3|) = min(2) = 2.
# It can be proven that 2 is the maximum tastiness that can be achieved.
# Example 3:

# Input: price = [7,7,7,7], k = 2
# Output: 0
# Explanation: Choosing any two distinct candies from the candies we have will result in a tastiness of 0.
 
# Constraints:

# 2 <= k <= price.length <= 105
# 1 <= price[i] <= 109

from typing import List

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        # WRONG ASSUMPTION - FAILURE
        # price.sort()
        # interval = (price[-1] - price[0]) / k
        # max_tastiness = float('inf')
        # prev_val = price[0]
        # prev_idx = 0
        # for _ in range(k - 1):
        #     cur_val = prev_val + interval
        #     cur_idx = bisect.bisect_left(price, cur_val)
            
        #     if cur_idx == prev_idx:
        #         cur_idx += 1
        #     elif cur_idx - 1 > prev_idx and abs(cur_val - price[cur_idx]) > abs(cur_val - price[cur_idx - 1]):
        #         cur_idx -= 1
        #     elif cur_idx + 1 < len(price) and abs(cur_val - price[cur_idx]) > abs(cur_val - price[cur_idx + 1]):
        #         cur_idx += 1

        #     max_tastiness = min(max_tastiness, price[cur_idx] - price[prev_idx])
            
        #     prev_idx = cur_idx
        #     prev_val = cur_val
            
        # return max_tastiness
        
        price.sort()
        
        def check(target: int) -> bool:
            prev = price[0]
            count = 1
            for i in range(1, len(price)):
                if price[i] - prev >= target:
                    count += 1
                    prev = price[i]
                    
                    if count == k:
                        return True
                    
            return False
        
        low = 0
        high = price[-1] - price[0]
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans