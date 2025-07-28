# 2367. Number of Arithmetic Triplets
# Easy
# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.

# Example 1:

# Input: nums = [0,1,4,6,7,10], diff = 3
# Output: 2
# Explanation:
# (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
# (2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 
# Example 2:

# Input: nums = [4,5,6,7,8,9], diff = 2
# Output: 2
# Explanation:
# (0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
# (1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.

# Constraints:

# 3 <= nums.length <= 200
# 0 <= nums[i] <= 200
# 1 <= diff <= 50
# nums is strictly increasing.

from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # count = 0
        # for i in range(len(nums) - 2):
        #     for j in range(i + 1, len(nums) - 1):
        #         d1 = nums[j] - nums[i]
        #         if d1 > diff:
        #             break
        #         if d1 == diff:
        #             for k in range(j + 1, len(nums)):
        #                 d2 = nums[k] - nums[j]
        #                 if d2 > diff:
        #                     break
        #                 if d2 == d1:
        #                     print(nums[i], nums[j], nums[k])
        #                     count += 1
        #                     break
        
        count = 0
        seen = set({nums[-1], nums[-2]})
        
        # c - b == b - a == d, where a, b, c, d == nums[i], nums[j], nums[k], diff and 0 <= i < j < k < len(nums)
        # => b = a + d and c = a + 2d
        d = diff
        for i in range(len(nums) - 3, -1, -1):
            a = nums[i]
            b = a + d
            c = a + 2 * d
            
            if b in seen and c in seen:
                count += 1
                
            seen.add(a)
                    
        return count
    
# solution = Solution()
# nums = [0,1,4,6,7,10]
# diff = 3
# nums = [4,5,6,7,8,9]
# diff = 2
# print(solution.arithmeticTriplets(nums, diff))