# 1498. Number of Subsequences That Satisfy the Given Sum Condition
# Medium
# You are given an array of integers nums and an integer target.

# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.
# Example 1:

# Input: nums = [3,5,6,7], target = 9
# Output: 4
# Explanation: There are 4 subsequences that satisfy the condition.
# [3] -> Min value + max value <= target (3 + 3 <= 9)
# [3,5] -> (3 + 5 <= 9)
# [3,5,6] -> (3 + 6 <= 9)
# [3,6] -> (3 + 6 <= 9)
# Example 2:

# Input: nums = [3,3,6,8], target = 10
# Output: 6
# Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
# [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
# Example 3:

# Input: nums = [2,3,3,4,6,7], target = 12
# Output: 61
# Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
# Number of valid subsequences (63 - 2 = 61).
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106
# 1 <= target <= 106

from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        def bs(begin, key):
            end = len(nums) - 1
            while True:
                mid = (begin + end) // 2
                if nums[mid] == key:
                    i = mid
                    while i < len(nums) and nums[i] == key:
                        i += 1
                    return i - 1
                elif nums[mid] > key:
                    end = mid - 1
                    if begin > end:
                        return end
                else:
                    begin = mid + 1
                    if begin > end:
                        return begin - 1
        
        subsequence_count = 0
        nums.sort()
        
        for i in range(len(nums)):
            end_value = target - nums[i]
            end_index = bs(i, end_value) if end_value >= nums[i] else i
            if end_index == i:
                if nums[i] <= target // 2:
                    subsequence_count += 1
            else:
                subsequence_count += 2 ** (end_index - i)

        return subsequence_count % (10 ** 9 + 7)
     
# nums = [3,5,6,7]
# nums = [3,3,6,8]
# target = 10
# target = 9   
# nums = [2,3,3,4,6,7]
# target = 12
# nums =[7,10,7,3,7,5,4]
# target = 12

# nums = [14,4,6,6,20,8,5,6,8,12,6,10,14,9,17,16,9,7,14,11,14,15,13,11,10,18,13,17,17,14,17,7,9,5,10,13,8,5,18,20,7,5,5,15,19,14]
# target = 22
# solution = Solution()
# print(solution.numSubseq(nums, target))