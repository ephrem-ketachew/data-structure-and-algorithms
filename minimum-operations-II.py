# 2170. Minimum Operations to Make the Array Alternating
# Medium

# You are given a 0-indexed array nums consisting of n positive integers.

# The array nums is called alternating if:

# nums[i - 2] == nums[i], where 2 <= i <= n - 1.
# nums[i - 1] != nums[i], where 1 <= i <= n - 1.
# In one operation, you can choose an index i and change nums[i] into any positive integer.

# Return the minimum number of operations required to make the array alternating.

# Example 1:

# Input: nums = [3,1,3,2,4,3]
# Output: 3
# Explanation:
# One way to make the array alternating is by converting it to [3,1,3,1,3,1].
# The number of operations required in this case is 3.
# It can be proven that it is not possible to make the array alternating in less than 3 operations. 
# Example 2:

# Input: nums = [1,2,2,2,2]
# Output: 2
# Explanation:
# One way to make the array alternating is by converting it to [1,2,1,2,1].
# The number of operations required in this case is 2.
# Note that the array cannot be converted to [2,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105

from typing import List
from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def get_max(counter: dict):
            first_freq, first_mode = 0, 0
            second_freq, second_mode = 0, 0
            
            for num, freq in counter.items():
                if freq > first_freq:
                    second_freq = first_freq
                    second_mode = first_mode
                    
                    first_freq = freq
                    first_mode = num
                elif freq > second_freq:
                    second_freq = freq
                    second_mode = num
                    
            return [(first_mode, first_freq), (second_mode, second_freq)]
                
        even_counter = Counter()
        odd_counter = Counter()
        
        odd_len = len(nums) // 2
        even_len = 1 + odd_len if len(nums) % 2 == 1 else odd_len
        
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_counter[num] += 1
            else:
                odd_counter[num] += 1
                
        even_max = get_max(even_counter)
        odd_max = get_max(odd_counter)
        
        if even_max[0][0] == odd_max[0][0]:
            case1 = even_len - even_max[1][1] + odd_len - odd_max[0][1]
            case2 = even_len - even_max[0][1] + odd_len - odd_max[1][1]
            
            return min(case1, case2)
        else:
            return even_len - even_max[0][1] + odd_len - odd_max[0][1]
        
        
# solution = Solution()
# nums = [3,1,3,2,4,3]
# nums = [1,2,2,2,2]
# nums = [1,3,4,3,3,2,3,3,2,2,3]
# print(solution.minimumOperations(nums))