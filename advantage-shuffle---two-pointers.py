# 870. Advantage Shuffle
# Medium
# You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

# Return any permutation of nums1 that maximizes its advantage with respect to nums2.

# Example 1:

# Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
# Output: [2,11,7,15]
# Example 2:

# Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
# Output: [24,32,8,12]

# Constraints:

# 1 <= nums1.length <= 105
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 109

from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        
        nums1.sort()
        nums2 = [(num, i) for i, num in enumerate(nums2)]
        nums2.sort()
        
        i = 0
        matched = []
        unmatched = []
        for (num, index) in nums2:
            while i < n and nums1[i] <= num:
                unmatched.append(nums1[i])
                i += 1
                
            if i < n:
                matched.append((nums1[i], index))
                i += 1
           
        matched.sort(key= lambda x: x[1])   
          
        ans = [0] * n
        j = k = 0
        for i in range(n):
            if j < len(matched) and matched[j][1] == i:
                ans[i] = matched[j][0]
                j += 1
            else:
                ans[i] = unmatched[k]
                k += 1
                
        return ans
    
# solution = Solution()
# nums1 = [2,7,11,15]
# nums2 = [1,10,4,11]
# nums1 = [12,24,8,32]
# nums2 = [13,25,32,11]
# print(solution.advantageCount(nums1, nums2))