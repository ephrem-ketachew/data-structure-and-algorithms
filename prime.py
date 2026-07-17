# 3896. Minimum Operations to Transform Array into Alternating Prime
# Medium

# You are given an integer array nums.

# An array is considered alternating prime if:

# Elements at even indices (0-based) are prime numbers.
# Elements at odd indices are non-prime numbers.
# In one operation, you may increment any element by 1.

# Return the minimum number of operations required to transform nums into an alternating prime array.

# A prime number is a natural number greater than 1 with only two factors, 1 and itself.

# Example 1:

# Input: nums = [1,2,3,4]

# Output: 3

# Explanation:

# The element at index 0 must be prime. Increment nums[0] = 1 to 2, using 1 operation.
# The element at index 1 must be non-prime. Increment nums[1] = 2 to 4, using 2 operations.
# The element at index 2 is already prime.
# The element at index 3 is already non-prime.
# Total operations = 1 + 2 = 3.

# Example 2:

# Input: nums = [5,6,7,8]

# Output: 0

# Explanation:

# The elements at indices 0 and 2 are already prime.
# The elements at indices 1 and 3 are already non-prime.
# No operations are needed.

# Example 3:

# Input: nums = [4,4]

# Output: 1

# Explanation:

# The element at index 0 must be prime. Increment nums[0] = 4 to 5, using 1 operation.
# The element at index 1 is already non-prime.
# Total operations = 1.

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        MAX_VALUE = 100005
        is_prime = [True] * MAX_VALUE
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(MAX_VALUE ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, MAX_VALUE, i):
                    is_prime[j] = False
            
        last_prime = -1
        next_prime = [-1] * MAX_VALUE
        for i in range(MAX_VALUE - 1, -1, -1):
            if is_prime[i]:
                last_prime = i
            next_prime[i] = last_prime
            
        last_non_prime = -1
        next_non_prime = [-1] * MAX_VALUE
        for i in range(MAX_VALUE - 1, -1, -1):
            if not is_prime[i]:
                last_non_prime = i
            next_non_prime[i] = last_non_prime
            
        count = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                count += next_prime[num] - num
            else:
                count += next_non_prime[num] - num
                
        return count