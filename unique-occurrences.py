# 1207. Unique Number of Occurrences
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:

# Input: arr = [1,2]
# Output: false
# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
from typing import List
from collections import Counter
 
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_counter = Counter(arr)
        return len(set(arr_counter.values())) == len(arr_counter.values())
        # seen = set()
        # for item in arr_counter:
        #     if arr_counter[item] in seen:
        #         return False
        #     seen.add(arr_counter[item])
            
        # return True