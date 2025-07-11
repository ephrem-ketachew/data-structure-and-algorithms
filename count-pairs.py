# 2364. Count Number of Bad Pairs

# You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

# Return the total number of bad pairs in nums.

# Example 1:

# Input: nums = [4,1,3,3]
# Output: 5
# Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
# The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
# The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
# The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
# The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
# There are a total of 5 bad pairs, so we return 5.
# Example 2:

# Input: nums = [1,2,3,4,5]
# Output: 0
# Explanation: There are no bad pairs.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= n

from typing import List
from math import comb

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # count_good_pairs = 0
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if j - i != nums[j] - nums[i]:
        #             count_bad_pairs += 1
        
        # return count_bad_pairs
        
        count_good_pairs = 0
        counter = {}
        count_total_pairs = comb(len(nums), 2)
        
        
        for i in range(len(nums)):
            diff = nums[i] - i
            counter[diff] = counter.setdefault(diff, 0) + 1
            
        for diff in counter:
            if counter[diff] > 1:
                count_good_pairs += comb(counter[diff], 2)
                
        return count_total_pairs - count_good_pairs
        
# nums = [4,1,3,3]
# nums = [1,2,3,4,5]
# solution = Solution()
# print(solution.countBadPairs(nums))