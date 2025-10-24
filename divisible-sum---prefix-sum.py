# 1590. Make Sum Divisible by P
# Medium
# Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

# Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

# A subarray is defined as a contiguous block of elements in the array.

# Example 1:

# Input: nums = [3,1,4,2], p = 6
# Output: 1
# Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
# Example 2:

# Input: nums = [6,3,5,2], p = 9
# Output: 2
# Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
# Example 3:

# Input: nums = [1,2,3], p = 3
# Output: 0
# Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= p <= 109

from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        tar_rem = sum(nums) % p
        if tar_rem == 0:
            return 0
        
        rem_map = {0: -1}
        min_len = n
        cur_rem = 0
        
        for i in range(n):
            cur_rem = (cur_rem + nums[i]) % p
            pre_rem = (cur_rem - tar_rem + p) % p
            
            if pre_rem in rem_map:
                length = i - rem_map[pre_rem]
                min_len = min(min_len, length)
                
            rem_map[cur_rem] = i
            
        return min_len if min_len < n else -1