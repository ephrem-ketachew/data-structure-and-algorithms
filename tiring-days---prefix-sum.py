# 1124. Longest Well-Performing Interval
# Medium

# We are given hours, a list of the number of hours worked per day for a given employee.

# A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

# A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

# Return the length of the longest well-performing interval.

# Example 1:

# Input: hours = [9,9,6,0,6,6,9]
# Output: 3
# Explanation: The longest well-performing interval is [9,9,6].
# Example 2:

# Input: hours = [6,6,6]
# Output: 0
 
# Constraints:

# 1 <= hours.length <= 104
# 0 <= hours[i] <= 16

from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        prefix = 0
        seen = {}
        max_len = 0
        for i in range(len(hours)):
            prefix += 1 if hours[i] > 8 else -1
            
            if prefix > 0:
                max_len = i + 1
            elif prefix - 1 in seen:
                max_len = max(max_len, i - seen[prefix - 1])
                
            if not prefix in seen:
                seen[prefix] = i
                
        return max_len