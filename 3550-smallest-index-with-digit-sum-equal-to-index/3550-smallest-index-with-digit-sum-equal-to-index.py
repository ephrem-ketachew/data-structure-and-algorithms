class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            digit_sum = 0
            for ch in str(num):
                digit_sum += int(ch)
                
            if digit_sum == i:
                return i
            
        return -1