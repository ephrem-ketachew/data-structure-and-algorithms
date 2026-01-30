# 2281. Sum of Total Strength of Wizards
# Hard

# As the ruler of a kingdom, you have an army of wizards at your command.

# You are given a 0-indexed integer array strength, where strength[i] denotes the strength of the ith wizard. For a contiguous group of wizards (i.e. the wizards' strengths form a subarray of strength), the total strength is defined as the product of the following two values:

# The strength of the weakest wizard in the group.
# The total of all the individual strengths of the wizards in the group.
# Return the sum of the total strengths of all contiguous groups of wizards. Since the answer may be very large, return it modulo 109 + 7.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: strength = [1,3,1,2]
# Output: 44
# Explanation: The following are all the contiguous groups of wizards:
# - [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
# - [3] from [1,3,1,2] has a total strength of min([3]) * sum([3]) = 3 * 3 = 9
# - [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
# - [2] from [1,3,1,2] has a total strength of min([2]) * sum([2]) = 2 * 2 = 4
# - [1,3] from [1,3,1,2] has a total strength of min([1,3]) * sum([1,3]) = 1 * 4 = 4
# - [3,1] from [1,3,1,2] has a total strength of min([3,1]) * sum([3,1]) = 1 * 4 = 4
# - [1,2] from [1,3,1,2] has a total strength of min([1,2]) * sum([1,2]) = 1 * 3 = 3
# - [1,3,1] from [1,3,1,2] has a total strength of min([1,3,1]) * sum([1,3,1]) = 1 * 5 = 5
# - [3,1,2] from [1,3,1,2] has a total strength of min([3,1,2]) * sum([3,1,2]) = 1 * 6 = 6
# - [1,3,1,2] from [1,3,1,2] has a total strength of min([1,3,1,2]) * sum([1,3,1,2]) = 1 * 7 = 7
# The sum of all the total strengths is 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44.
# Example 2:

# Input: strength = [5,4,6]
# Output: 213
# Explanation: The following are all the contiguous groups of wizards: 
# - [5] from [5,4,6] has a total strength of min([5]) * sum([5]) = 5 * 5 = 25
# - [4] from [5,4,6] has a total strength of min([4]) * sum([4]) = 4 * 4 = 16
# - [6] from [5,4,6] has a total strength of min([6]) * sum([6]) = 6 * 6 = 36
# - [5,4] from [5,4,6] has a total strength of min([5,4]) * sum([5,4]) = 4 * 9 = 36
# - [4,6] from [5,4,6] has a total strength of min([4,6]) * sum([4,6]) = 4 * 10 = 40
# - [5,4,6] from [5,4,6] has a total strength of min([5,4,6]) * sum([5,4,6]) = 4 * 15 = 60
# The sum of all the total strengths is 25 + 16 + 36 + 36 + 40 + 60 = 213.

# Constraints:

# 1 <= strength.length <= 105
# 1 <= strength[i] <= 109

from typing import List

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        # n = len(strength)
        # # spent 4+ hours on wrong assumption😭
        # # sum of all subarrays sum from [l, r], l <= r
        # # summation of nums[i] * (i - l + 1) * (r - i + 1) for i in range(l, r + 1) cuz each nums[i] contributes (i - l + 1) * (r - i + 1) times to the total sum
        # # this can be rewritten as  sum(nums[i] * (-i * i + (l + r)i + (r + 1)(1 - l)) for i in range(l, r + 1))
        # # so we need to store 3 prefix sums for i * i * nums[i], i * nums[i], nums[i]
        
        # prefix_square = [0] * (n + 1)
        # prefix_linear = [0] * (n + 1)
        # prefix_constant = [0] * (n + 1)
        
        # for i in range(n):
        #     prefix_square[i + 1] = prefix_square[i] + strength[i] * i * i
        #     prefix_linear[i + 1] = prefix_linear[i] + strength[i] * i
        #     prefix_constant[i + 1] = prefix_constant[i] + strength[i]
            
        # strength = strength + [float('-inf')]
        # stack = []
        # total_strength_sum = 0
        # for i, cur_strength in enumerate(strength):
        #     while stack and strength[stack[-1]] > cur_strength:
        #         mid_idx = stack.pop()
                
        #         left_bound = stack[-1] if stack else -1
        #         right_bound = i
                
        #         count = (mid_idx - left_bound) * (right_bound - mid_idx)
                
        #         # sum(nums[i] * (-i * i + (l + r)i + (r + 1)(1 - l))
        #         left_bound += 1
        #         right_bound -= 1
        #         square_sum = prefix_square[right_bound + 1] - prefix_square[left_bound]
        #         linear_sum = prefix_linear[right_bound + 1] - prefix_linear[left_bound]
        #         constant_sum = prefix_constant[right_bound + 1] - prefix_constant[left_bound]
                
        #         subarray_sum = -square_sum + (left_bound + right_bound) * linear_sum + (right_bound + 1) * (1 - left_bound) * constant_sum
                
        #         total_strength_sum += count * subarray_sum
                
                
        #     stack.append(i)
            
        # return total_strength_sum
        
        n = len(strength)
        
        MOD = 10 ** 9 + 7
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + strength[i]
            
        prefix_prefix = [0] * (n + 2)
        for i in range(n + 1):
            prefix_prefix[i + 1] = prefix_prefix[i] + prefix[i]   
            
        strength = strength + [float('-inf')]
        stack = []
        total_strength_sum = 0
        for i, cur_strength in enumerate(strength):
            while stack and strength[stack[-1]] > cur_strength:
                mid_idx = stack.pop()
                
                left_bound = stack[-1] + 1 if stack else 0
                right_bound = i - 1
                
                subarray_sum = (mid_idx - left_bound + 1) * (prefix_prefix[right_bound + 2] - prefix_prefix[mid_idx + 1]) - (right_bound - mid_idx + 1) * (prefix_prefix[mid_idx + 1] - prefix_prefix[left_bound])
                
                total_strength_sum += strength[mid_idx] * subarray_sum
                
                
            stack.append(i)
            
        return total_strength_sum % MOD
    
    
# s = Solution()
# nums = [2, 3, 5, 1, 8, 5, 4, 9]
# print(s.totalStrength(nums))