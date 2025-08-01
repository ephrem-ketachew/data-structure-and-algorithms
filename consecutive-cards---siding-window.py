# 2260. Minimum Consecutive Cards to Pick Up
# Medium
# You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

# Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

# Example 1:

# Input: cards = [3,4,2,3,4,7]
# Output: 4
# Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.
# Example 2:

# Input: cards = [1,0,5,3]
# Output: -1
# Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.

# Constraints:

# 1 <= cards.length <= 105
# 0 <= cards[i] <= 106

from typing import List
# from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # if len(set(cards)) == len(cards):
        #     return -1
        
        # counter = defaultdict(int)
        # min_pick, left = len(cards), 0
        
        # for right in range(len(cards)):
        #     counter[cards[right]] += 1
            
        #     while counter[cards[right]] > 1:
        #         counter[cards[left]] -= 1
        #         if counter[cards[left]] == 0:
        #             del counter[cards[left]]
                    
        #         min_pick = min(min_pick, right - left + 1)
        #         left += 1
                
        # return min_pick
        
        seen = {}
        min_pick = float('inf')
        
        for i in range(len(cards)):
            if cards[i] in seen:
                min_pick = min(min_pick, i - seen[cards[i]] + 1)
                
            seen[cards[i]] = i
        
        return min_pick if min_pick != float('inf') else -1
        