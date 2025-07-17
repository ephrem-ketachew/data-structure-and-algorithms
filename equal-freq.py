# 1224. Maximum Equal Frequency
# Hard
# Given an array nums of positive integers, return the longest possible length of an array prefix of nums, such that it is possible to remove exactly one element from this prefix so that every number that has appeared in it will have the same number of occurrences.

# If after removing one element there are no remaining elements, it's still considered that every appeared number has the same number of ocurrences (0).

# Example 1:

# Input: nums = [2,2,1,1,5,3,3,5]
# Output: 7
# Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4] = 5, we will get [2,2,1,1,3,3], so that each number will appear exactly twice.
# Example 2:

# Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
# Output: 13

# Constraints:

# 2 <= nums.length <= 105
# 1 <= nums[i] <= 105

from typing import List
from collections import Counter

class Solution:    
    def maxEqualFreq(self, nums: List[int]) -> int:
        max_len = 0
        counter = Counter()
        freq_counter = Counter()
        max_freq = 0
        count_max = 0
        
        for i, num in enumerate(nums):
            old_freq = counter[num]
            new_freq = old_freq + 1
            counter[num] += 1
            
            if old_freq > 0:
                freq_counter[old_freq] -= 1
                if freq_counter[old_freq] == 0:
                    del freq_counter[old_freq]
            freq_counter[new_freq] += 1
            
            if counter[num] > max_freq:
                max_freq = counter[num]
                count_max = 1
            elif counter[num] == max_freq:
                count_max += 1
                
            if len(counter) == i + 1:
                max_len = i + 1
                continue
            
            min_freq = min(freq_counter.keys())
            
            if len(counter) == 1:
                max_len = i + 1
                continue
            
            if freq_counter[1] == 1:
                if max_freq * count_max == i:
                    max_len = i + 1
                
            if max_freq == min_freq + 1:
                if count_max == 1:
                    max_len = i + 1
                    
        
        return max_len
    
# solution = Solution()
# nums = [2,2,1,1,5,3,3,5]
# nums = [1,2,3,1,2,3,4,4,4,4,1,2,3,5,6]
# nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
# print(solution.maxEqualFreq(nums))
            