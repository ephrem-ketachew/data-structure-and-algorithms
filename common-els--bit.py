# 2032. Two Out of Three
# Easy

# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.

# Example 1:

# Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
# Output: [3,2]
# Explanation: The values that are present in at least two arrays are:
# - 3, in all three arrays.
# - 2, in nums1 and nums2.
# Example 2:

# Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
# Output: [2,3,1]
# Explanation: The values that are present in at least two arrays are:
# - 2, in nums2 and nums3.
# - 3, in nums1 and nums2.
# - 1, in nums1 and nums3.
# Example 3:

# Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
# Output: []
# Explanation: No value is present in at least two arrays.

# Constraints:

# 1 <= nums1.length, nums2.length, nums3.length <= 100
# 1 <= nums1[i], nums2[j], nums3[k] <= 100

from typing import List

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # nums1_set, nums2_set, nums3_set = set(nums1), set(nums2), set(nums3)
        # common = []
        # for num in nums1_set.union(nums2_set):
        #     if num in nums3_set or (num in nums1_set and num in nums2_set):
        #         common.append(num)
                
        # return common
        
        # s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        # return list((s1 & s2) | (s1 & s3) | (s2 & s3))
        
        mask = {}
        for x in nums1:
            mask[x] = mask.get(x, 0) | 1
        
        for x in nums2:
            mask[x] = mask.get(x, 0) | 2
        
        for x in nums3:
            mask[x] = mask.get(x, 0) | 4
            
        return [x for x, m in mask.items() if m.bit_count() >= 2]
    