# 923. 3Sum With Multiplicity
# Medium
# Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

# As the answer can be very large, return it modulo 109 + 7.

# Example 1:

# Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation: 
# Enumerating by the values (arr[i], arr[j], arr[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.
# Example 2:

# Input: arr = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation: 
# arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.
# Example 3:

# Input: arr = [2,1,3], target = 6
# Output: 1
# Explanation: (1, 2, 3) occured one time in the array so we return 1.

# Constraints:

# 3 <= arr.length <= 3000
# 0 <= arr[i] <= 100
# 0 <= target <= 300

from typing import List
import bisect
from collections import Counter
from math import comb

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        # first apporach, works(ac'd) but a lot of complexity and less efficient
        # UPPER_BOUND = 10 ** 9 + 7
        # count = 0

        # arr.sort()
        # for i in range(len(arr) - 2):
        #     num = arr[i]
        #     if num > target:
        #         continue
            
        #     t = target - num
        #     left, right = i + 1, len(arr) - 1
        #     while left < right:
        #         summ = arr[left] + arr[right]
                
        #         if summ == t:
        #             end = bisect.bisect_right(arr, arr[left], hi=right) - 1
        #             count += end - left + 1
        #             count %= UPPER_BOUND
        #             right -= 1
        #         elif summ < t:
        #             left += 1
        #         else:
        #             right -= 1
                    
        # return count
            
        # efficient solution
        MOD = 10 ** 9 + 7
        counter = Counter(arr)
        keys = sorted(counter.keys())
        
        count = 0
        for i, num in enumerate(keys):
            if  num > target:
                break
            
            t = target - num
            left, right = i, len(keys) - 1
            while left <= right:
                summ = keys[left] + keys[right]
                
                if summ < t:
                    left += 1
                elif summ > t:
                    right -= 1
                else:
                    if i < left < right:
                        count += counter[keys[i]] * counter[keys[left]] * counter[keys[right]]
                    elif i == left < right:
                        count += comb(counter[keys[i]], 2) * counter[keys[right]]
                    elif i < left == right:
                        count += counter[keys[i]] * comb(counter[keys[left]], 2)
                    else:
                        count += comb(counter[keys[i]], 3)
                        
                    left += 1
                    right -= 1
                    
        return count % MOD
                
                
            
solution = Solution()
arr = [1,1,2,2,3,3,4,4,5,5]
target = 8
arr = [1,1,2,2,2,2]
target = 5
arr = [2,1,3]
target = 6
print(solution.threeSumMulti(arr, target))