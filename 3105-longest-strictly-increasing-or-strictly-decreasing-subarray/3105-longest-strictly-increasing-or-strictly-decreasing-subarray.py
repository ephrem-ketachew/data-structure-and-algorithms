class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc_left = dec_left = 0
        max_len = 1
        
        for right in range(1, len(nums)):
            if nums[right] == nums[right - 1]:
                inc_left = dec_left = right
            elif nums[right] > nums[right - 1]:
                dec_left = right
            else:
                inc_left = right
                
            max_len = max(max_len, right - dec_left + 1, right - inc_left + 1)
            
        return max_len