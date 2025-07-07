# 718. Maximum Length of Repeated Subarray
# Medium

# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

# Example 1:

# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
# Example 2:

# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
# Explanation: The repeated subarray with maximum length is [0,0,0,0,0].

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100

from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # easy- intuitive yet inefficient and tle
        
        # nums2_set = set(nums2)
        # max_length = 0
        
        # for i in range(len(nums1)):
        #     if nums1[i] in nums2_set:
        #         for j in range(len(nums2)):
        #             if nums1[i] == nums2[j]:
        #                 length = 0
        #                 left = i
        #                 right = j
        #                 while left < len(nums1) and right < len(nums2):
        #                     if nums1[left] == nums2[right]:
        #                         length += 1
        #                     else:
        #                         break
        #                     left += 1
        #                     right +=1
        #                 max_length = max(max_length, length)
                        
        # return max_length
        
        
        # dp -- efficient yet hard unless you get familiar with dp
        # m, n = len(nums1), len(nums2)
        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        # max_len = 0
        
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if nums1[i - 1] == nums2[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1] + 1
        #             max_len = max(max_len, dp[i][j])
        
        # return max_len
        
        
        # here comes the most counter intuitive approach with sliding window
        def max_length(offset_nums1, offset_nums2, length):
            max_len = 0
            cur_len = 0
            for i in range(length):
                if nums1[i + offset_nums1] == nums2[i + offset_nums2]:
                    cur_len += 1
                    max_len = max(max_len, cur_len)
                else:
                    cur_len = 0
                    
            return max_len
        
        m, n = len(nums1), len(nums2)
        maximum_length = 0
        for offset in range(-m + 1, n):
            offset_nums1 = max(0, -offset)
            offset_nums2 = max(0, offset)
            length = min(m - offset_nums1, n - offset_nums2)
            maximum_length = max(maximum_length, max_length(offset_nums1, offset_nums2, length))
            
        return maximum_length
    
    
# solution = Solution()
# nums1 = [1,2,3,2,1]
# nums2 = [3,2,1,4,7]
# print(solution.findLength(nums1, nums2))