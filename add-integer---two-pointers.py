# 3132. Find the Integer Added to Array II
# Medium
# You are given two integer arrays nums1 and nums2.

# From nums1 two elements have been removed, and all other elements have been increased (or decreased in the case of negative) by an integer, represented by the variable x.

# As a result, nums1 becomes equal to nums2. Two arrays are considered equal when they contain the same integers with the same frequencies.

# Return the minimum possible integer x that achieves this equivalence.

# Example 1:

# Input: nums1 = [4,20,16,12,8], nums2 = [14,18,10]

# Output: -2

# Explanation:

# After removing elements at indices [0,4] and adding -2, nums1 becomes [18,14,10].

# Example 2:

# Input: nums1 = [3,5,5,3], nums2 = [7,7]

# Output: 2

# Explanation:

# After removing elements at indices [0,3] and adding 2, nums1 becomes [7,7].

# Constraints:

# 3 <= nums1.length <= 200
# nums2.length == nums1.length - 2
# 0 <= nums1[i], nums2[i] <= 1000
# The test cases are generated in a way that there is an integer x such that nums1 can become equal to nums2 by removing two elements and adding x to each element of nums1.

from typing import List

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        # min_add = float('inf')
        # nums1.sort()
        # nums2.sort()
        # for i in range(len(nums1) - 1):
        #     for j in range(i + 1, len(nums1)):
        #         p = q = 0
        #         diff = None
        #         valid = True
        #         while p < len(nums1) and q < len(nums2):
        #             if p == i or p == j:
        #                 p += 1
        #                 continue
        #             if diff is None:
        #                 diff = nums2[q] - nums1[p]
                        
        #             if diff >= min_add or nums2[q] - nums1[p] != diff:
        #                 valid = False
        #                 break
                    
        #             p += 1
        #             q += 1
                    
        #         if valid:
        #             min_add = diff
                    
        # return min_add
        
        nums1.sort()
        nums2.sort()
        min_add = float('inf')
        for i in range(3):
            k, j = i, 0
            diff = nums2[0] - nums1[k]
            while k < len(nums1) and j < len(nums2):
                if nums2[j] - nums1[k] == diff:
                    j += 1
                k += 1
            if j == len(nums2): 
                min_add = min(min_add, diff)  
          
        return min_add
    
# solution = Solution()
# nums1 = [4,20,16,12,8]
# nums2 = [14,18,10]
# print(solution.minimumAddedInteger(nums1, nums2))