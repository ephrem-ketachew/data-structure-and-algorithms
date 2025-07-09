# 992. Subarrays with K Different Integers
# Hard

# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A good array is an array where the number of different integers in that array is exactly k.

# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

# Example 1:

# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
# Example 2:

# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# 1 <= nums[i], k <= nums.length

from typing import List
# from collections import Counter
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # count, left = 0, 0
        # counter = Counter()
        # for right in range(len(nums)):
        #     counter[nums[right]] += 1
        #     while len(counter) > k:
        #         counter[nums[left]] -= 1
        #         if counter[nums[left]] == 0:
        #             del counter[nums[left]]
        #         left += 1
                
        #     if len(counter) == k:
        #         c = counter.copy()
        #         for i in range(left, right + 1):
        #             count += 1
        #             c[nums[i]] -= 1
        #             if c[nums[i]] == 0:
        #                 break
                
        # return count
        
        def subarraysWithAtMostKDistinct(k):
            count, left = 0, 0
            counter = defaultdict(int)
            for right in range(len(nums)):
                counter[nums[right]] += 1
                while len(counter) > k:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        del counter[nums[left]]
                    left += 1
                    
                count += right - left + 1  
                
            return count
        
        return subarraysWithAtMostKDistinct(k) - subarraysWithAtMostKDistinct(k - 1)
    
# solution = Solution()
# nums = [1,2,1,3,4]
# k = 3
# print(solution.subarraysWithKDistinct(nums, k))