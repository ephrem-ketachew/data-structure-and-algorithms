# 1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number
# Medium
# You are given a string num, representing a large integer, and an integer k.

# We call some integer wonderful if it is a permutation of the digits in num and is greater in value than num. There can be many wonderful integers. However, we only care about the smallest-valued ones.

# For example, when num = "5489355142":
# The 1st smallest wonderful integer is "5489355214".
# The 2nd smallest wonderful integer is "5489355241".
# The 3rd smallest wonderful integer is "5489355412".
# The 4th smallest wonderful integer is "5489355421".
# Return the minimum number of adjacent digit swaps that needs to be applied to num to reach the kth smallest wonderful integer.

# The tests are generated in such a way that kth smallest wonderful integer exists.

# Example 1:

# Input: num = "5489355142", k = 4
# Output: 2
# Explanation: The 4th smallest wonderful number is "5489355421". To get this number:
# - Swap index 7 with index 8: "5489355142" -> "5489355412"
# - Swap index 8 with index 9: "5489355412" -> "5489355421"
# Example 2:

# Input: num = "11112", k = 4
# Output: 4
# Explanation: The 4th smallest wonderful number is "21111". To get this number:
# - Swap index 3 with index 4: "11112" -> "11121"
# - Swap index 2 with index 3: "11121" -> "11211"
# - Swap index 1 with index 2: "11211" -> "12111"
# - Swap index 0 with index 1: "12111" -> "21111"
# Example 3:

# Input: num = "00123", k = 1
# Output: 1
# Explanation: The 1st smallest wonderful number is "00132". To get this number:
# - Swap index 3 with index 4: "00123" -> "00132"

# Constraints:

# 2 <= num.length <= 1000
# 1 <= k <= 1000
# num only consists of digits.

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def next_permutation(nums: list):
            pivot_index, n = -1, len(nums)
            for i in range(n - 2, -1, -1):
                if nums[i + 1] > nums[i]:
                    pivot_index = i
                    break
                
            if pivot_index == -1:
                nums.reverse()
                return
            
            for j in range(n - 1, pivot_index, -1):
                if nums[j] > nums[pivot_index]:
                    nums[j], nums[pivot_index] = nums[pivot_index], nums[j]
                    break
                
            left, right = pivot_index + 1, n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
            
        nums = [int(ch) for ch in num]
        original_nums = nums[:]
        for i in range(k):
            next_permutation(nums)
            
        min_swaps = 0  
        for i in range(len(nums)):
            if nums[i] == original_nums[i]:
                continue
            
            for j in range(i + 1, len(nums)):
                if nums[j] == original_nums[i]:
                    break
            
            for index in range(j, i, -1):
                nums[index], nums[index - 1] = nums[index - 1], nums[index]
                min_swaps += 1
                
        return min_swaps
        
# solution = Solution()
# num = "5489355142"
# k = 4
# num = "11112"
# k = 4
# num = "00123"
# k = 1
# print(solution.getMinSwaps(num, k))