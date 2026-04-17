# # 3761. Minimum Absolute Distance Between Mirror Pairs
# Medium

# You are given an integer array nums.

# A mirror pair is a pair of indices (i, j) such that:

# 0 <= i < j < nums.length, and
# reverse(nums[i]) == nums[j], where reverse(x) denotes the integer formed by reversing the digits of x. Leading zeros are omitted after reversing, for example reverse(120) = 21.
# Return the minimum absolute distance between the indices of any mirror pair. The absolute distance between indices i and j is abs(i - j).

# If no mirror pair exists, return -1.

# Example 1:

# Input: nums = [12,21,45,33,54]

# Output: 1

# Explanation:

# The mirror pairs are:

# (0, 1) since reverse(nums[0]) = reverse(12) = 21 = nums[1], giving an absolute distance abs(0 - 1) = 1.
# (2, 4) since reverse(nums[2]) = reverse(45) = 54 = nums[4], giving an absolute distance abs(2 - 4) = 2.
# The minimum absolute distance among all pairs is 1.

# Example 2:

# Input: nums = [120,21]

# Output: 1

# Explanation:

# There is only one mirror pair (0, 1) since reverse(nums[0]) = reverse(120) = 21 = nums[1].

# The minimum absolute distance is 1.

# Example 3:

# Input: nums = [21,120]

# Output: -1

# Explanation:

# There are no mirror pairs in the array.

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109​​​​​​​

from typing import List
from collections import defaultdict

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        rev_nums = [int(str(num)[::-1]) for num in nums]
        seen = defaultdict(int)
        min_dist = float('inf')
        for i, num in enumerate(rev_nums):
            if nums[i] in seen:
                min_dist = min(min_dist, i - seen[nums[i]])
                
            seen[num] = i
            
        return min_dist if min_dist != float('inf') else -1