# 3318. Find X-Sum of All K-Long Subarrays I
# Easy
# You are given an array nums of n integers and two integers k and x.

# The x-sum of an array is calculated by the following procedure:

# Count the occurrences of all elements in the array.
# Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
# Calculate the sum of the resulting array.
# Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

# Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].

# Example 1:

# Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

# Output: [6,10,12]

# Explanation:

# For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
# For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
# For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.
# Example 2:

# Input: nums = [3,8,7,8,7,5], k = 2, x = 2

# Output: [11,15,15,15,12]

# Explanation:

# Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

# Constraints:

# 1 <= n == nums.length <= 50
# 1 <= nums[i] <= 50
# 1 <= x <= k <= nums.length

from typing import List
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def top_k_elements(count, l, k):
            bucket = [[] for _ in range(l + 1)]
            
            for num, freq in count.items():
                bucket[freq].append(num)
                
            res, length = 0, 0
            for i in range(len(bucket) - 1, -1, -1):
                if length + len(bucket[i]) > k:
                    bucket[i].sort()
                    for j in range(len(bucket[i]) - 1, -1, -1):
                        num = bucket[i][j]
                        res += num * count[num]
                        length += 1
                        if length == k:
                            return res
                for num in bucket[i]:
                    res += num * count[num]
                    length += 1
                    if length == k:
                        return res
                    
            return res
        
        
        
        length = len(nums) - k + 1
        count = Counter(nums[:k])
        x_sum = [0] * length
        x_sum[0] = top_k_elements(count, k, x)
        
        for i in range(1, length):
            count[nums[i + k - 1]] += 1
            count[nums[i - 1]] -= 1
            if count[nums[i - 1]] == 0:
                del count[nums[i - 1]]
            x_sum[i] = top_k_elements(count, k, x)
            
        return x_sum
                
# solution = Solution()
# nums = [1,1,2,2,3,4,2,3]
# k = 6
# x = 2

# nums = [3,8,7,8,7,5]
# k = 2
# x = 2

# nums = [50,50,50,50,50,50]
# k = 6
# x = 1
# print(solution.findXSum(nums, k, x))