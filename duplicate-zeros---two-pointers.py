# 1089. Duplicate Zeros
# Easy
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

# Example 1:

# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
# Example 2:

# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]

# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 9

from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        # store = []
        # j = 0
        # for i in range(len(arr)):
        #     if arr[i] == 0:
        #         store.append(0)
        #     if j < len(store):
        #         store.append(arr[i])
        #         arr[i] = store[j]
        #         j += 1
          
        # i = 0   
        # while i < len(arr):
        #     print(arr)
        #     if arr[i] == 0:
        #         for j in range(len(arr) - 1, i, -1):
        #             arr[j] = arr[j - 1]
        #         i += 1
        #     i += 1
        
        count_dup_zeros = 0
        n = len(arr)
        
        for i in range(len(arr)):
            if i + count_dup_zeros >= n:
                break
            if arr[i] == 0:
                if i + count_dup_zeros == n - 1:
                    arr[-1] = 0
                    n -= 1
                    break
                count_dup_zeros += 1
             
        i = n - 1
        j = n - 1 - count_dup_zeros
        while j >= 0:
            if arr[j] == 0:
                arr[i] = 0
                i -= 1
                arr[i] = 0
                i -= 1
            else:
                arr[i] = arr[j]
                i -= 1
            j -= 1

                    
# solution = Solution()
# arr = [1,0,2,3,0,4,5,0]
# arr = [8,4,5,0,0,0,0,7]
# print(solution.duplicateZeros(arr))