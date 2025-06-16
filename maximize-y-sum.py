# Q1. Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values
# Medium
# 4 pt.
# You are given two integer arrays x and y, each of length n. You must choose three distinct indices i, j, and k such that:

# x[i] != x[j]
# x[j] != x[k]
# x[k] != x[i]
# Your goal is to maximize the value of y[i] + y[j] + y[k] under these conditions. Return the maximum possible sum that can be obtained by choosing such a triplet of indices.

# If no such triplet exists, return -1.

# Example 1:

# Input: x = [1,2,1,3,2], y = [5,3,4,6,2]

# Output: 14

# Explanation:

# Choose i = 0 (x[i] = 1, y[i] = 5), j = 1 (x[j] = 2, y[j] = 3), k = 3 (x[k] = 3, y[k] = 6).
# All three values chosen from x are distinct. 5 + 3 + 6 = 14 is the maximum we can obtain. Hence, the output is 14.
# Example 2:

# Input: x = [1,2,1,2], y = [4,5,6,7]

# Output: -1

# Explanation:

# There are only two distinct values in x. Hence, the output is -1.
 

# Constraints:

# n == x.length == y.length
# 3 <= n <= 105
# 1 <= x[i], y[i] <= 106

from typing import List

class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        first_max = [None, None, None]
        second_max = [None, None, None]
        third_max = [None, None, None]
        
        for i in range(len(y)):
            if first_max[0] is None or y[i] > first_max[0]:
                first_max[0] = y[i]
                first_max[1] = i
                first_max[2] = x[i]
                
        for i in range(len(y)):
            if (second_max[0] is None and i != first_max[1] and x[i] != first_max[2]) or (second_max[0] is not None and y[i] >  second_max[0] and i != first_max[1] and x[i] != first_max[2]):
                second_max[0] = y[i]
                second_max[1] = i
                second_max[2] = x[i]
                
        for i in range(len(y)):
            if (third_max[0] is None and (second_max[0] is not None and i != first_max[1] and x[i] != first_max[2] and i != second_max[1] and x[i] != second_max[2])) or (second_max[0] is not None and third_max[0] is not None and y[i] >  third_max[0] and (i != first_max[1] and x[i] != first_max[2] and i != second_max[1] and x[i] != second_max[2])):
                third_max[0] = y[i]
                third_max[1] = i
                third_max[2] = x[i]
                
        if first_max[1] is not None and second_max[1] is not None and third_max[1] is not None:
            return first_max[0] + second_max[0] + third_max[0]
                
        return -1
